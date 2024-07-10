import mysql.connector
from mysql.connector import Error

# 查詢 django_admin_log 的紀錄
def query_django_admin_log(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM django_admin_log"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("django_admin_log 紀錄:")
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

# 查詢 user_activitylogs 的紀錄
def query_user_activitylogs(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM user_activitylogs"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("user_activitylogs 紀錄:")
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

def main():
    try:
        connection = mysql.connector.connect(
            host='140.131.114.242',
            database='113-ntub113209',
            user='ntub113209',
            password='Sw@23110565'
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            # 查詢紀錄
            query_django_admin_log(connection)
            query_user_activitylogs(connection)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print('MySQL連線已關閉')

if __name__ == "__main__":
    main()
