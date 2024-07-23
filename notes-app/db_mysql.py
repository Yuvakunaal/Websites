import pymysql

def connect():
    con = pymysql.connect(host='ocdb.app',port=5051,database='db_42kvdb39f',user='user_42kvdb39f',password='p42kvdb39f')
    return con 
def noteTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS notes(
        id integer primary key AUTO_INCREMENT,
        title varchar(255) not null,
        notes varchar(2000) not null
    )"""
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Note:
    def __init__(self, id=None,title='',notes=''):
        self.id = id 
        self.title = title 
        self.notes = notes
    def __str__(self):
        return f'[{self.id},{self.title},{self.notes}]'
    def __repr__(self):
        return self.__str__()

def createNote(note):
    sql = """INSERT INTO notes(title, notes) VALUES(%s,%s)"""
    params = (note.title, note.notes,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  #
    con.commit()
    con.close()
    return id           #

def readAllNotes():
    sql = """SELECT id,title, notes FROM notes"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = cur.fetchall() #[rows], each row=[id,title,...]
    con.close()

    notes = []
    for row in result:
        notes.append(Note(id=row[0],title=row[1],
                notes=row[2]))
    return notes 

def updateNote(note):
    sql = """UPDATE notes set title=%s,notes=%s WHERE (id=%s)"""
    params = (note.title, note.notes,
              note.id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()

def deleteNote(id):
    sql = """DELETE from notes WHERE (id=%s)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()

def readNoteById(id):
    sql = """SELECT id,title, notes FROM notes WHERE (id=%s)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = cur.fetchone() #row=[id,title,...]
    con.close()

    if result != None:
        note = Note(id=result[0],title=result[1],
                    notes=result[2])
    else:
        note = None 
    return note

def searchNote(title,notes_text):
    title = title.strip()
    notes_text = notes_text.strip()
    sql = '''SELECT id,title,notes FROM notes 
    WHERE (%s != '' AND title = %s) OR
          (%s != '' AND notes like ('%'||%s||'%')) OR
          (%s == '' AND %s == '')
    '''
    params = (title,title,notes_text,notes_text,title,notes_text)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = cur.fetchall()
    con.close()

    notes = []
    for row in result:
        notes.append(Note(id=row[0],title=row[1],
                notes=row[2]))
    return notes 


