from sqlite3 import connect, Error



def AddInsert(name, url):
    try:
        con = connect("../vocie.db")
        cursor = con.cursor()
        cursor.execute("""insert into voicebot(name, url) values(?, ?)""", (name, url))
        con.commit()
    except (Error, Exception) as error:
        print("xato", error)
    finally:
        if con:
            cursor.close()
            con.close()
            print("tugadi")


def ReadVoice(name):
    try:
        con = connect("../vocie.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM voicebot WHERE name LIKE ?", (name + '%',))
        results = cursor.fetchall()
        return  results
    except (Error, Exception) as error:
        print("xato:", error)
    finally:
        if con:
            cursor.close()
            con.close()
            print("tugadi")


def DeleteVoices(name):
    try:
        con = connect("../vocie.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM voicebot WHERE name = ?", (name,))
        con.commit()
    except (Error, Exception) as error:
        print("xato", error)
    finally:
        if con:
            cursor.close()
            con.close()
            print("tugadi")


#
# try:
#     con = connect("vocie.db")
#     cursor = con.cursor()
#     cursor.execute("""
#                     create table Voicebot(
#                     ID INTEGER PRIMARY KEY NoT NULL,
#                     NAME TEXT NOT NULL,
#                     URL TEXT NOT NULL);
#                                         """)
#     con.commit()
# except (Error, Exception) as error:
#     print("xato", error)
# finally:
#     if con:
#         cursor.close()
#         con.close()
#         print("tugadi")