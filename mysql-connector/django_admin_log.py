import mysql.connector
from mysql.connector import Error
from datetime import datetime

# 插入到 django_admin_log
def insert_into_django_admin_log(connection, user, action, email):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO django_admin_log (user_id, content_type_id, object_id, object_repr, action_flag, change_message, action_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (user, None, None, None, action, email, timestamp))
        connection.commit()
        print("紀錄已插入到 django_admin_log")
    except Error as e:
        print(f"Error: {e}")

# 插入到 user_activitylogs
def insert_into_user_activitylogs(connection, user, activity, email):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO user_activitylogs (user, activity, email, timestamp) VALUES (%s, %s, %s, %s)"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (user, activity, email, timestamp))
        connection.commit()
        print("紀錄已插入到 user_activitylogs")
    except Error as e:
        print(f"Error: {e}")

# 查詢 django_admin_log
def query_django_admin_log(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM django_admin_log"
        cursor.execute(sql)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

# 查詢 user_activitylogs
def query_user_activitylogs(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM user_activitylogs"
        cursor.execute(sql)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print(f"Error: {e}")

# 範例紀錄
records = [
    ('張三', '新增角色', 'zhangsan@example.com'),
    ('李四', '刪除角色', 'lisi@example.com')
]

activities = [
    ('張三', '新增角色', 'zhangsan@example.com'),
    ('李四', '刪除角色', 'lisi@example.com')
]

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

            # 插入紀錄
            for record in records:
                insert_into_django_admin_log(connection, *record)
            
            for activity in activities:
                insert_into_user_activitylogs(connection, *activity)
            
            # 查詢紀錄
            print("\nDjango_admin_log 紀錄:")
            query_django_admin_log(connection)

            print("\nUser_activitylogs 紀錄:")
            query_user_activitylogs(connection)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print('MySQL連線已關閉')

if __name__ == "__main__":
    main()
