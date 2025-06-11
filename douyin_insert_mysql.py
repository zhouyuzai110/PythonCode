import os
import pymysql
from datetime import datetime

# 配置数据库连接
DB_CONFIG = {'host': '192.168.1.5', 'user': 'flaskapi', 'password': 'qwe123!@#', 'database': 'flaskapi', 'charset': 'utf8mb4'}

# 文件夹路径（Linux路径格式）
FOLDER_PATH = r'//ttnas/homes/zy0612/douyin_download/'


def parse_filename(filename):
    """解析文件名并返回结构化数据"""
    try:
        # 移除文件扩展名
        basename = os.path.splitext(filename)[0]

        # 分割文件名各部分
        parts = basename.split('_')
        if len(parts) < 7:
            raise ValueError("文件名格式不符合要求")

        # 提取基础信息
        author_id = parts[0]
        author_name = parts[1]

        # 拼接日期时间并转换格式
        date_part = parts[2]
        time_part = f"{parts[3]}:{parts[4]}:{parts[5]}"
        creation_time = f"{date_part} {time_part}"

        # 验证时间格式
        datetime.strptime(creation_time, "%Y-%m-%d %H:%M:%S")

        # 生成时间戳
        dt = datetime.strptime(creation_time, "%Y-%m-%d %H:%M:%S")
        timestamp = int(dt.timestamp())

        # 合并作品标题（处理可能包含的下划线）
        aweme_name = '_'.join(parts[6:])

        return {
            'author_id': author_id,
            'author_name': author_name,
            'creation_time': creation_time,
            'aweme_name': aweme_name,
            'aweme_total_name': filename,
            'aweme_timestamp': timestamp
        }
    except Exception as e:
        print(f"解析失败 {filename}: {str(e)}")
        return None


def main():
    try:
        # Connect to the database using context manager
        with pymysql.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                inserted_count = 0

                # Iterate over files in folder path
                for filename in os.listdir(FOLDER_PATH):
                    if not filename.endswith(('.mp4', '.webp')):
                        continue

                    data = parse_filename(filename)
                    if not data:
                        continue

                    # Check if record already exists
                    check_sql = "SELECT COUNT(*) FROM dyaweme WHERE aweme_total_name = %s"
                    cursor.execute(check_sql, (data['aweme_total_name'], ))
                    exists = cursor.fetchone()[0]

                    if exists == 0:
                        insert_sql = """
                            INSERT INTO dyaweme (
                                author_id,
                                author_name,
                                creation_time,
                                aweme_name,
                                aweme_total_name,
                                aweme_timestamp
                            ) VALUES (%s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(insert_sql, (data['author_id'], data['author_name'], data['creation_time'],
                                                    data['aweme_name'], data['aweme_total_name'], data['aweme_timestamp']))
                        inserted_count += 1
                    # else:
                    #     print(f"跳过重复文件: {data['aweme_total_name']}")

                conn.commit()
                print(f"成功插入 {inserted_count} 条记录")

    except Exception as e:
        print(f"数据库操作失败: {str(e)}")
    # finally:
    #     conn.close()


if __name__ == '__main__':
    main()
