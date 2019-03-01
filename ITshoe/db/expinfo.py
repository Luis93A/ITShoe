#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql as sql

def Connect_DB():
        try:
            db=sql.connect(host = 'localhost', user = 'root', passwd = 'shinobi39', db = 'itshoedata', port =3306 )
            
            return db 

        except:
            print("Deu erro")
			
			
def Disconnect_DB():
        try:
            #cur.close()
            db.close()
            
        except:
            print("Error closing DB COM")
			
def insert_register(db):
	db.query("INSERT INTO EXPinfo VALUES ('01-03-2019','experiencia tal','info','info',info')")

	
def create_table(db):
	db.query("CREATE TABLE IF NOT EXISTS EXPinfo (Date varchar(15) DEFAULT NULL,info varchar(150) DEFAULT NULL,other1 int(150) DEFAULT NULL,other2 int(150) DEFAULT NULL,other3 int(150) DEFAULT NULL)")		

db = Connect_DB()
print(db)

create_table(db)

insert_register(db)
#db.commit()


#cur.execute("TRUNCATE TABLE registos")