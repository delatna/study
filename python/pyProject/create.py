#file name : create.py

import sqlite3     #SQL Light : SQLight -> SQLight ->sqllite

def create_table():
    conn = sqlite3.connect("first.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE book_table (
            idx     integer primary key,
            title   text,
            author  text,
            price   integer
        )
    
    ''')

    conn.commit()
    conn.close()

# 무조건 실행
#create_table()

#python create.py 이렇게 실행 할때만 실행되도록 함
#파이참에서 실행 명령으로 실행이 안되게 함
if __name__ == "__main__":
    create_table()
