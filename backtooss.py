import os
import oss2
from flask import Flask
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)
NAMESPACE = '/ossBackup'
auth = oss2.Auth('<your-access-key-id>', '<your-access-key-secret>')
bucket = oss2.Bucket(auth, 'https://oss-cn-region.aliyuncs.com', 'your-bucket-name')
def backup_to_oss(local_paths, overwrite=False):
    """
    将指定本地路径下的文件备份到OSS。

    :param local_paths: 要备份的本地目录列表
    :param overwrite: 是否覆盖OSS上已存在的文件（默认 False，增量备份）
    """
    for local_path in local_paths:
        for root, dirs, files in os.walk(local_path):
            for file_name in files:
                local_file_path = os.path.join(root, file_name)
                oss_object_key = os.path.relpath(local_file_path, start=local_path)

                try:
                    # 如果非覆盖模式，且OSS已存在该文件，则跳过
                    if not overwrite and bucket.object_exists(oss_object_key):
                        socketio.emit('message', {
                            'status': 'skipped',
                            'file': local_file_path
                        }, namespace=NAMESPACE)
                        continue

                    # 使用多线程上传大文件
                    oss2.resumable_upload(
                        bucket,
                        oss_object_key,
                        local_file_path,
                        num_threads=4,
                        progress_callback=oss2.make_progress_adapter(
                            lambda consumed_bytes, total_bytes: socketio.emit('message', {
                                'status': 'uploading',
                                'file': local_file_path,
                                'progress': f'{consumed_bytes}/{total_bytes}'
                            }, namespace=NAMESPACE)
                        )
                    )
                    socketio.emit('message', {
                        'status': 'uploaded',
                        'file': local_file_path
                    }, namespace=NAMESPACE)
                except Exception as e:
                    socketio.emit('message', {
                        'status': 'error',
                        'file': local_file_path,
                        'error': str(e)
                    }, namespace=NAMESPACE)

    socketio.emit('backup_complete', {'message': 'Backup process completed.'}, namespace=NAMESPACE)
@socketio.on('connect', namespace=NAMESPACE)
def handle_connect():
    print('Client connected')

@socketio.on('start_backup', namespace=NAMESPACE)
def handle_start_backup(data):
    local_directories = data.get('directories', [])
    backup_to_oss(local_directories)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    



const socket = io.connect('http://localhost:5000/ossBackup');


socket.on('message', function(data) {
    console.log(`Status: ${data.status}, File: ${data.file}`);
    if (data.error) {
        console.error(`Error: ${data.error}`);
    }
});

socket.on('backup_complete', function(data) {
    console.log(data.message);
});
// 连接到 OSS 备份命名空间
const socket = io('http://localhost:5000/ossBackup');

// 触发全量备份（增量备份时省略 overwrite 字段或设为 false）
socket.emit('start_backup', {
    directories: ['/path/to/local/folder1', '/path/to/local/folder2'],
    overwrite: true  // 传入 true 表示全量覆盖上传
});



@socketio.on('start_backup', namespace=NAMESPACE)
def handle_start_backup(data):
    local_directories = data.get('directories', [])
    overwrite = data.get('overwrite', False)  # 新增这一行，读取 overwrite 参数
    backup_to_oss(local_directories, overwrite=overwrite)  # 传入 overwrite 参数

    

// Connect to the 'ossBackup' namespace
const socket = io('http://localhost:5000/ossBackup');

// Trigger the 'start_backup' event and send a list of directories
socket.emit('start_backup', {
    directories: [
        '/path/to/local/folder1',
        '/path/to/local/folder2'
    ]
});



def restore_from_oss(remote_prefix, local_root):
    """
    从 OSS 下载指定前缀的所有文件到本地目录

    :param remote_prefix: OSS 上文件的前缀（相当于目录）
    :param local_root: 本地保存路径根目录
    """
    try:
        # 获取远程 OSS 文件列表
        for obj in oss2.ObjectIterator(bucket, prefix=remote_prefix):
            remote_key = obj.key
            
            # 增加路径匹配检查，避免非目标前缀的文件被处理
            if not remote_key.startswith(remote_prefix):
                continue

            # 构建本地文件路径，保留原始目录结构
            local_file_path = os.path.join(local_root, os.path.relpath(remote_key, remote_prefix))

            # 确保本地目录存在
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

            # 检查本地是否已存在该文件
            if os.path.exists(local_file_path):
                socketio.emit('message', {
                    'status': 'skipped',
                    'file': local_file_path
                }, namespace=NAMESPACE)
                continue

            try:
                # 使用多线程下载大文件
                oss2.resumable_download(
                    bucket,
                    remote_key,
                    local_file_path,
                    num_threads=4,  # 启用并发下载
                    progress_callback=oss2.make_progress_adapter(
                        lambda consumed_bytes, total_bytes: socketio.emit('message', {
                            'status': 'downloading',
                            'file': local_file_path,
                            'progress': f'{consumed_bytes}/{total_bytes}'
                        }, namespace=NAMESPACE)
                    )
                )
                socketio.emit('message', {
                    'status': 'restored',
                    'file': local_file_path
                }, namespace=NAMESPACE)
            except Exception as e:
                socketio.emit('message', {
                    'status': 'error',
                    'file': local_file_path,
                    'error': str(e)
                }, namespace=NAMESPACE)
    except Exception as e:
        socketio.emit('message', {
            'status': 'error',
            'file': '',
            'error': f'Failed to list files from OSS: {str(e)}'
        }, namespace=NAMESPACE)

    socketio.emit('restore_complete', {'message': 'Restore process completed.'}, namespace=NAMESPACE)


@socketio.on('start_restore', namespace=NAMESPACE)
def handle_start_restore(data):
    remote_prefix = data.get('remote_prefix', '')  # OSS 上的路径
    local_directory = data.get('local_directory', '')  # 本地保存路径
    if not remote_prefix or not local_directory:
        socketio.emit('message', {'status': 'error', 'error': 'Missing parameters'}, namespace=NAMESPACE)
        return
    restore_from_oss(remote_prefix, local_directory)


const socket = io('http://localhost:5000/ossBackup');

socket.emit('start_restore', {
    remote_prefix: 'your/remote/prefix/',   // OSS 上的目录
    local_directory: '/path/to/local/dir'   // 本地要还原的目录
});