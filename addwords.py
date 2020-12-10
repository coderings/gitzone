#! /usr/bin/python3.8
import sys
import mysql.connector as mysql

class mysqlconnect():
    def __init__(self, host, port, password, filename ):
        self.host = host
        self.port =  port
        self.password = password
        self.filename=filename
        self.mydb = mysql.connect(host=self.host,user="root",password=self.password,port=self.port,database="mydb")
        self.mycursor=self.mydb.cursor()

    def getLineNumber(self, word ):
        print(word)
        for n,line in enumerate(open(self.filename)):
            if word==line:
                return n

    def getLastRow(self ):
       #look for the highest id with this tag and return the word
       sql="SELECT word  FROM passwords  ORDER BY id DESC LIMIT 0, 1;"
       self.mycursor.execute(sql)
       result = self.mycursor.fetchall()[0][0] 
       if len(result)>0:
            return result

    def addToSQL(self,  lineNo):
        print(lineNo)
        file = open(self.filename,'r', encoding='utf8' )
        for n,  line in enumerate( file.readlines()):
            if int(n) >  int(lineNo):
                mycursor=self.mydb.cursor()
                sql = "insert into passwords(word,tags) values('{}','{}');".format(line, self.filename) 
                print(sql)
                mycursor.execute(sql)
                mydb.commit()
                mycursor.close()

filename='rockyou.txt'
hello= mysqlconnect("localhost","6603","abc", filename)
lastSQL=hello.getLastRow()
lineNo=hello.getLineNumber(lastSQL )
hello.addToSQL(lineNo)

