import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="universe",
    password="franchise",
    database="dc_vs_marvel"
)

# Open a file to write the data to
with open('output.txt', 'w') as file:
    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM actor")

    # Fetch all the rows and write them to the file
    rows = cursor.fetchall()
    for row in rows:
        file.write(str(row) + "\n")
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
