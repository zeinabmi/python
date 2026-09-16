import mariadb

icao = input("Anna lentoaseman ICAO-koodi: ")

conn = mariadb.connect(
    host="localhost",
    user="zizii",
    database="airportdb"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT name, municipality FROM airport WHERE ident = ?",
    (icao,)
)

result = cursor.fetchone()

if result:
    print("Lentokenttä:", result[0])
    print("Sijaintikunta:", result[1])
else:
    print("Lentokenttää ei löytynyt.")

conn.close()