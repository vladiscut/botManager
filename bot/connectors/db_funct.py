import sqlite3


conn = sqlite3.connect('db.db')

def create_table_user():
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER UNIQUE, name INTEGER);""")
    cur.close()
    conn.commit()
    
def create_table_cart():
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, item TEXT DEFAULT NULL);""")
    cur.close()
    conn.commit()

def check_cart(user_id):
    cur = conn.cursor()
    cart_data = cur.execute("""select * from cart where user_id=?""", [user_id]).fetchall()
    cur.close()
    conn.commit()

def create_user(user_id,user_first_name):
    cur = conn.cursor()
    cur.execute("""INSERT OR IGNORE into users (user_id, name) VALUES (?, ?)""", [user_id, user_first_name])
    cur.close()
    conn.commit()

def add_to_cart(user_id,caption):
    cur = conn.cursor()
    cur.execute("""INSERT into cart (user_id, item) VALUES (?, ?)""", [user_id, caption])
    cur.close()
    conn.commit()

def clean_cart(user_id):
    cur = conn.cursor()
    cur.execute("""delete from cart where user_id=?""",  [user_id]).fetchall()
    cur.close()
    conn.commit()