import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )
cur = conn.cursor()

# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
# 
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
# 
# 
# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
# 
# cur.execute("delete from student where age='9'")
# 
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
#     ])
# 
# 
# cur.fetchone()
cur.execute("select * from status1")

cur.fetchone()

info = cur.fetchmany("select * from status1")
for ii in info:
    print (ii)
    
    
cur.close()
conn.commit()
conn.close()