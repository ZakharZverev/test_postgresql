import psycopg2

con=psycopg2.connect(database='clients', user='zakhar', password='12345', host="127.0.0.1", port="9090")
print('Database opened')

cur=con.cursor()

cur.execute("INSERT INTO CLIENTS(ID,NAME,AGE,COURSE) VALUES (001,'Kolya','18', 'E-cars')")

con.commit()
print('Data inserted')
con.close()

