import pymysql

def get_connection():
    try: 
        return pymysql.connect(
            host='localhost',
            database='galeriadearte',
            user='root',
            password='',
            
        )

    except Exception as ex:
        print(ex)

  