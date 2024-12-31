import sqlite3
import sys
import os


def query_star_file(db_path):
    # 检查文件是否存在
    if not os.path.isfile(db_path):
        print(f"文件 {db_path} 不存在。")
        return

    try:
        # 连接到 SQLite 数据库
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 查询 gis_info_table 中 star = 1 的记录
        query = "SELECT file_name FROM gis_info_table WHERE star = 1;"
        cursor.execute(query)
        results = cursor.fetchall()

        # 关闭连接
        conn.close()

        # 输出结果
        if results:
            print("收藏的文件名：")
            for file_path in results:
                # 提取文件名
                file_name = os.path.basename(file_path[0])
                print(file_name)
        else:
            print("未找到 star = 1 的记录。")
    except sqlite3.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请将 .db 文件拖入本程序！")
    else:
        db_file = sys.argv[1]
        query_star_file(db_file)

    # 等待用户按下任意键关闭
    input("\n按下任意键退出...")