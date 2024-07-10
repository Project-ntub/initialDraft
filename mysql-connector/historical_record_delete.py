import mysql.connector
from mysql.connector import Error

# 刪除 django_admin_log 的紀錄
def delete_from_django_admin_log(connection, user):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM django_admin_log WHERE user_id = %s"
        cursor.execute(sql, (user,))
        connection.commit()
        print(f"django_admin_log 中 user_id 為 {user} 的紀錄已刪除")
    except Error as e:
        print(f"Error: {e}")

# 刪除 user_activitylogs 的紀錄
def delete_from_user_activitylogs(connection, user):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM user_activitylogs WHERE user = %s"
        cursor.execute(sql, (user,))
        connection.commit()
        print(f"user_activitylogs 中 user 為 {user} 的紀錄已刪除")
    except Error as e:
        print(f"Error: {e}")

def main():
    users_to_delete = ['張三', '李四']  # 要刪除的用戶

    try:
        connection = mysql.connector.connect(
            host='140.131.114.242',
            database='113-ntub113209',
            user='ntub113209',
            password='Sw@23110565'
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            # 刪除紀錄
            for user in users_to_delete:
                delete_from_django_admin_log(connection, user)
                delete_from_user_activitylogs(connection, user)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print('MySQL連線已關閉')

if __name__ == "__main__":
    main()
