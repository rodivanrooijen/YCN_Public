import mysql.connector #pip install mysql-connector-python

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="voorbeeld_db"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM fiets")
myresult = mycursor.fetchall()

# print resultaten van het aantal versnellingen
print("De fietsen hebben de volgende versnellingen: ")
for x in myresult:
    print(x[2])

# Specificeer de gegevens van de nieuwe fiets
merk = 'Trek'
versnellingen = '16'
bouw_datum = '2020-12-22'
foto = 'mijnfiets8.jpg'

# Voeg de nieuwe fiets toe aan de database
insert_query = f"INSERT INTO fiets (id, merk, aantal_versnellingen, bouw_datum, foto) VALUES (NULL, '{merk}', '{versnellingen}', '{bouw_datum}', '{foto}')"
mycursor.execute(insert_query)
mydb.commit()
print("Nieuwe registratie in de database succesvol!")

# Print de laatst toegevoegde fiets
mycursor.execute('SELECT * FROM fiets ORDER BY id DESC LIMIT 1')
last_inserted_row = mycursor.fetchone()
print("De laatste fiets in de database is: ")
print(last_inserted_row)