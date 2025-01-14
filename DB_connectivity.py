import mysql.connector

# Connect to MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",         # Your database host
        user="kaveri",            # Your MySQL username
        password="root18",        # Your MySQL password
        database="attendance_db"  # Your database name
    )
    c = conn.cursor()
    print("Database connection successful.")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# Function to record attendance in the database
def record_attendance(name):
    try:
        # Check if attendance is already marked for the name
        c.execute("SELECT * FROM attendance WHERE name = %s", (name,))
        if not c.fetchone():  # If no record exists
            c.execute("INSERT INTO attendance (name, status) VALUES (%s, %s)", (name, 'present'))
            conn.commit()
            print(f"Attendance marked for {name}.")
        else:
            print(f"Attendance already marked for {name}.")
    except mysql.connector.Error as e:
        print(f"Error inserting attendance: {e}")

# Example usage - change name to "Kaveri"
record_attendance("Kaveri")

# Close the connection when done
conn.close()
