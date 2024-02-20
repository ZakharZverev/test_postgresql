import psycopg2

con=psycopg2.connect(database='clients', user='zakhar', password='12345', host="127.0.0.1", port="9090")
print('Database opened')

cur=con.cursor()

cur.execute("SELECT ID, NAME, AGE, COURSE FROM CLIENTS WHERE AGE > %s", (18)) #make SQL request

rows=cur.fetchall() #get results

for row in rows:
    print(row[0]) # ID
    print(row[1]) # NAME
    print(row[2]) # AGE
    print(row[3]) # COURSE

print("Operation completed")
con.close()
