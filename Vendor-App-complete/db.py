import sqlite3

def connect():
    con = sqlite3.connect('vendor_db.db')
    return con 
def vendorTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS vendors(
        id integer primary key AUTOINCREMENT,
        name varchar(255) not null,
        location varchar(2000) not null,
        type varchar(255) not null,
        rating varchar(255) not null
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Vendor:
    def __init__(self, id=None,name='',location='',type='',rating=''):
        self.id = id 
        self.name = name
        self.location = location
        self.type = type
        self.rating = rating
    def __str__(self):
        return f'[{self.id},{self.name},{self.location},{self.type},{self.rating}]'
    def __repr__(self):
        return self.__str__()

def createVendor(vendor):
    sql = """INSERT INTO vendors(name, location, type, rating)
    VALUES(?,?,?,?)"""
    params = (vendor.name, vendor.location,vendor.type,vendor.rating)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  
    con.commit()
    con.close()
    return id           

def readAllVendors():
    sql = """SELECT id,name,location,type,rating FROM vendors"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    vendors = []
    for row in result:
        vendors.append(Vendor(id=row[0],name=row[1],
                location=row[2],type=row[3],rating=row[4]))
    return vendors 

def updateVendor(vendor):
    sql = """UPDATE vendors
    set name=?,location=?,type=?,rating=?
    WHERE (id=?)"""
    params = (vendor.name, vendor.location,vendor.type,vendor.rating,
              vendor.id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()

def deleteVendor(id):
    sql = """DELETE from vendors
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readVendorById(id):
    sql = """SELECT id,name, location,type,rating FROM vendors
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone() #row=[id,title,...]
    con.close()

    if result != None:
        vendor = Vendor(id=result[0],name=result[1],
                    location=result[2],type=result[3],rating=result[4])
    else:
        vendor = None 
    return vendor

def searchVendor(name,location,type,rating):
    name = name.strip()
    location = location.strip()
    type = type.strip()
    rating = rating.strip()
    sql = '''SELECT id,name,location,type,rating FROM vendors 
    WHERE (? != '' AND name = ?) OR
          (? != '' AND location like ('%'||?||'%')) OR
          (? != '' AND type like ('%'||?||'%')) OR
          (? != '' AND rating = ?) OR
          (? == '' AND ? == '' AND ? == '' AND ? == '')
    '''
    params = (name,name,location,location,type,type,rating,rating,name,location,type,rating)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall()
    con.close()

    vendors = []
    for row in result:
        vendors.append(Vendor(id=row[0],name=row[1],
                location=row[2],type=row[3],rating=row[4]))
    return vendors