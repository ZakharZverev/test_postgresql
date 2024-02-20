import psycopg2

con=psycopg2.connect(database='clients', user='zakhar', password='12345', host="127.0.0.1", port="9090")
print('Database opened')

cur=con.cursor()

cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (001,'Kolya','19', 'E-cars')")
cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (002,'Vova','19', 'Languages')")
cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (003,'Olya','17', 'Physics')")
cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (004,'Zakhar','18', 'E-cars')")
cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (005,'Georgiy','19', 'Math')")
cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (006,'Misha','19', 'IT')")

con.commit()
print('Data inserted')
con.close()

