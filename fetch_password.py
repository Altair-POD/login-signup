import sqlite3




#command = "CREATE TABLE info_pass (ID INTEGER PRIMARY KEY AUTOINCREMENT, USER_NAME TEXT NOT NULL, EMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL)"
#command = f"insert into info_pass (USER_NAME, EMAIL, PASSWORD) values('{name}', '{email}', '{passwd}')"
#conn.commit()

def come_passwd(user_name):

    conn = sqlite3.connect("user_info.db")
    command = f"select password from info_pass where user_name='{user_name}'"

    cursor = conn.execute(command)
    r = cursor.fetchall()
    if(len(r) == 0):
        return -1
    else:
        return r[0][0]

    conn.close()


print(come_passwd("wow"))







