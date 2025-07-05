import mysql.connector
import time

def connect_to_mysql():
    print("Connecting to MySQL...")
    attempts = 0
    while attempts < 5:
        try:
            return mysql.connector.connect(
                host="mysql_db",
                user="user",
                password="password",
                database="mydb"
            )
        except mysql.connector.Error as err:
            attempts += 1
            print(f"Attempt {attempts}/5 failed: {err}")
            time.sleep(3)
    raise RuntimeError("Failed to connect to MySQL after 5 attempts")

if __name__ == "__main__":
    db = connect_to_mysql()
    cursor = db.cursor()
    
    # 执行查询
    cursor.execute("SELECT message FROM test_table")
    result = cursor.fetchone()
    print(f"Database message: {result[0]}")
    
    # 插入新数据
    cursor.execute("INSERT INTO test_table (message) VALUES ('Hello from Python!')")
    db.commit()
    
    cursor.close()
    db.close()
    print("Operation completed successfully!")