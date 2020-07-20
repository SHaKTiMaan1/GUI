import sqlite3
conn = sqlite3.connect("child.db")
c = conn.cursor()


c.execute('''drop table details ''')
c.execute('''drop table attendance ''')
conn.commit()
