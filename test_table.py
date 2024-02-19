import psycopg2

con=psycopg2.connect(database='clients', user='zakhar', password='12345', host="127.0.0.1", port="9090")
print('Database opened')

cur=con.cursor()

cur.execute(''' CREATE TABLE CLIENTS
        (ID  INT PRIMARYKEY      NOT NULL,
        NAME        TEXT        NOT NULL,
        AGE         INT         NOT NULL,
        COURSE      CHAR(50));


            ''')
print('Database created')

con.commit()
cur.close()
con.close()