#!/usr/bin/env python3
import argparse
import os
import time
from getpass import getpass

import paramiko
from scp import SCPClient


def create_ssh_client(host, port, username, key_path):
    """创建 SSH 客户端连接"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 尝试使用密钥认证
        client.connect(hostname=host, port=port, username=username, key_filename=key_path, timeout=10)
        print(f"✅ 使用密钥 {key_path} 成功连接到 {host}")
        return client
    except paramiko.ssh_exception.SSHException:
        # 如果密钥失败，尝试密码认证
        password = getpass(f"输入 {username}@{host} 的密码: ")
        client.connect(hostname=host, port=port, username=username, password=password, timeout=10)
        print(f"✅ 使用密码成功连接到 {host}")
        return client
    except Exception as e:
        print(f"❌ 连接失败: {str(e)}")
        exit(1)


def upload_and_deploy(ssh_client, local_archive, remote_dir):
    """上传文件并部署容器"""
    with SCPClient(ssh_client.get_transport()) as scp:
        # 上传压缩文件
        remote_archive = os.path.join(remote_dir, os.path.basename(local_archive))
        print(f"⬆️ 上传文件: {local_archive} -> {remote_archive}")
        scp.put(local_archive, remote_archive)

        # 在远程主机执行命令
        commands = [
            f"mkdir -p {remote_dir}", f"tar -xzvf {remote_archive} -C {remote_dir}",
            f"find {remote_dir} -type f \( -name '*.yaml' -o -name '*.yml' \) -print0 | "
            f"xargs -0 -I {{}} sh -c 'echo \"🚀 启动: $1\" && podman-compose -f \"$1\" up -d' _ {{}}"
        ]

        for cmd in commands:
            print(f"🔧 执行命令: {cmd}")
            stdin, stdout, stderr = ssh_client.exec_command(cmd)

            # 实时输出命令结果
            print("--- 输出开始 ---")
            for line in stdout:
                print(line.strip())
            for line in stderr:
                print(f"⚠️ 错误: {line.strip()}")
            print("--- 输出结束 ---")
            time.sleep(1)

        print("✅ 所有操作已完成！")


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='部署 Podman Compose 项目到远程主机')
    parser.add_argument('archive', help='本地压缩文件路径 (e.g., target.tar.gz)')
    parser.add_argument('--host', default='192.168.1.9', help='目标主机 IP')
    parser.add_argument('--port', type=int, default=22, help='SSH 端口')
    parser.add_argument('--user', default='core', help='SSH 用户名')
    parser.add_argument('--key', default='~/.ssh/id_rsa', help='SSH 私钥路径')
    parser.add_argument('--dir', default='/opt/podman', help='远程主机部署目录')
    args = parser.parse_args()

    # 展开路径中的 ~
    args.key = os.path.expanduser(args.key)
    args.archive = os.path.expanduser(args.archive)

    # 验证文件存在
    if not os.path.exists(args.archive):
        print(f"❌ 错误: 文件 {args.archive} 不存在")
        exit(1)

    # 创建 SSH 连接
    print(f"🔗 连接到 {args.user}@{args.host}:{args.port}...")
    ssh = create_ssh_client(args.host, args.port, args.user, args.key)

    # 上传并部署
    try:
        upload_and_deploy(ssh, args.archive, args.dir)
    finally:
        # 确保关闭连接
        ssh.close()
        print("🔒 SSH 连接已关闭")


if __name__ == "__main__":
    main()
"""
# 基本用法
python deploy-podman.py target.tar.gz

# 自定义参数
python deploy-podman.py target.tar.gz \
  --host=192.168.1.10 \
  --user=admin \
  --key=~/.ssh/custom_key \
  --dir=/opt/deployments


$ python deploy-podman.py ~/projects/compose-bundle.tar.gz --host=192.168.1.9

🔗 连接到 core@192.168.1.9:22...
✅ 使用密钥 ~/.ssh/id_rsa 成功连接到 192.168.1.9
⬆️ 上传文件: /home/user/projects/compose-bundle.tar.gz -> /opt/podman/compose-bundle.tar.gz
🔧 执行命令: mkdir -p /opt/podman
--- 输出开始 ---
--- 输出结束 ---
🔧 执行命令: tar -xzvf /opt/podman/compose-bundle.tar.gz -C /opt/podman
--- 输出开始 ---
app1/docker-compose.yml
app2/podman-compose.yaml
app3/compose.yml
--- 输出结束 ---
🔧 执行命令: find /opt/podman -type f \( -name '*.yaml' -o -name '*.yml' \) -print0 | xargs -0 -I {} sh -c 'echo "🚀 启动: $1" && podman-compose -f "$1" up -d' _ {}
--- 输出开始 ---
🚀 启动: /opt/podman/app1/docker-compose.yml
Creating network "app1_default" with the default driver
Creating container1 ... done
🚀 启动: /opt/podman/app2/podman-compose.yaml
Creating network "app2_default" with the default driver
Creating service1 ... done
🚀 启动: /opt/podman/app3/compose.yml
Creating network "app3_default" with the default driver
Creating web ... done
--- 输出结束 ---
✅ 所有操作已完成！
🔒 SSH 连接已关闭
"""
