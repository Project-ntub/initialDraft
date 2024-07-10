import mysql.connector
from mysql.connector import Error
from datetime import datetime

# 修改 django_admin_log 的紀錄
def update_django_admin_log(connection, user, new_action, new_email):
    try:
        cursor = connection.cursor()
        sql = "UPDATE django_admin_log SET action_flag = %s, change_message = %s, action_time = %s WHERE user_id = %s"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (new_action, new_email, timestamp, user))
        connection.commit()
        print(f"django_admin_log 中 user_id 為 {user} 的紀錄已修改")
    except Error as e:
        print(f"Error: {e}")

# 修改 user_activitylogs 的紀錄
def update_user_activitylogs(connection, user, new_activity, new_email):
    try:
        cursor = connection.cursor()
        sql = "UPDATE user_activitylogs SET activity = %s, email = %s, timestamp = %s WHERE user = %s"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (new_activity, new_email, timestamp, user))
        connection.commit()
        print(f"user_activitylogs 中 user 為 {user} 的紀錄已修改")
    except Error as e:
        print(f"Error: {e}")

def main():
    modifications = [
        ('張三', '更新角色', 'new_zhangsan@example.com'),
        ('李四', '更新角色', 'new_lisi@example.com')
    ]

    try:
        connection = mysql.connector.connect(
            host='140.131.114.242',
            database='113-ntub113209',
            user='ntub113209',
            password='Sw@23110565'
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            # 修改紀錄
            for user, new_action, new_email in modifications:
                update_django_admin_log(connection, user, new_action, new_email)
                update_user_activitylogs(connection, user, new_action, new_email)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print('MySQL連線已關閉')

if __name__ == "__main__":
    main()
