import sqlite3

conn = sqlite3.connect('shop.db')
curr = conn.cursor()
name = 'pizza'
price = 449

curr.execute('''CREATE TABLE "product" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"price"   INTEGER
	PRIMARY KEY("id" AUTOINCREMENT)
)''')
curr.execute(f'INSERT INTO product(name,price) values ("{name}",{price})')
data = curr.execute("SELECT * FROM product").fetchall()
print(data)
conn.commit()

conn.close()