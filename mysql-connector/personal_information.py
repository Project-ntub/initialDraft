import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='140.131.114.242',
            database='113-ntub113209',
            user='ntub113209',
            password='Sw@23110565'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def get_user_profile(user_id):
    connection = create_connection()
    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT name, username, department, position, phone, email, created FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_profile = cursor.fetchone()
        return user_profile
    except Error as e:
        print(f"Error reading data from MySQL table: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_user_profile(user_id, name, username, department, position, phone, email):
    connection = create_connection()
    if connection is None:
        return False

    cursor = connection.cursor()
    try:
        query = """
        UPDATE users
        SET name = %s, username = %s, department = %s, position = %s, phone = %s, email = %s
        WHERE id = %s
        """
        cursor.execute(query, (name, username, department, position, phone, email, user_id))
        connection.commit()
        return True
    except Error as e:
        print(f"Error updating data in MySQL table: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage:
user_id = 1
profile = get_user_profile(user_id)
if profile:
    print("User Profile:", profile)
else:
    print("Failed to retrieve user profile.")

# Example of updating a user profile
updated = update_user_profile(user_id, "New Name", "newusername", "新部門", "新職位", "0987654321", "newemail@example.com")
if updated:
    print("User profile updated successfully.")
else:
    print("Failed to update user profile.")
