import pymssql

conn = pymssql.connect(
    server="localhost", user="sa", password="1", database="DiscordRPG"
)


def readDB(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from RPGLogonData where userID=%s", id)
    if cursor.rowcount > 0:
        return cursor
    else:
        return "no such user, create one?"


def insertDB(userID, userName, characterName):
    cursor = conn.cursor()
    cursor.execute(
        "insert into [RPGLogonData](userID,userName,characterName,level,career)values(%s,%s,%s,%s,%s)",
        (userID, userName, characterName, str(1), "")
    )
    conn.commit()


def updateDB(id):
    cursor = conn.cursor()
    cursor.execute("update SC set xxx where id=%s", id)
    return "update completed!"


def deleteDB():
    cursor = conn.cursor()
    cursor.execute("delete * from SC where @id = id")
    return "delete completed!"
