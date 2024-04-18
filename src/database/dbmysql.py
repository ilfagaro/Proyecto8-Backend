import pymysql

def get_connection():
    try: 
        return pymysql.connect(
            host='localhost',
            db='galeriadearte',
            user='root',
            password='',
            
        )

    except Exception as ex:
        print(ex)

  