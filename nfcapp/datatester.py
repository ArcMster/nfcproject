import sqlite3

conn = sqlite3.connect('C:\\Users\\PSSRE\\projects\\nfcproject\\db.sqlite3')

results = conn.execute("SELECT * FROM nfcapp_stories")
for row in results:
    print(row[3])

conn.close()