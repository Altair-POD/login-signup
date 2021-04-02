import sqlite3


def to_database(user_name, email, password):
    conn = sqlite3.connect("user_info.db")
    command = f"select * from info_pass where user_name='{user_name}'"
    cursor = conn.execute(command)
    r = cursor.fetchall()
    if(len(r)!=0):
        return -1
    else:
        command = f"insert into info_pass (USER_NAME, EMAIL, PASSWORD) values('{user_name}', '{email}', '{password}')"
        conn.execute(command)
        conn.commit()
    conn.close()



