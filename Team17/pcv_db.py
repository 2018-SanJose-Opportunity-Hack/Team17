import sqlite3
import pandas
conn = sqlite3.connect('pcvdata.db')

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE pcv_matches
 #            (advisor_name text, advisor_phone text, advisor_email text, sbo_name text, sbo_email text, sbo_phone text, interview_date text, interview_time text)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

#df = pandas.read_csv('pcv_data.csv')
#df.to_sql('pcv_matches', conn, if_exists='append', index=False)

c.execute('SELECT advisor_email, sbo_email FROM pcv_matches')
print (c.fetchall())

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()