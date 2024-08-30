import sqlite3

# Connect to the database
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# cur.execute('''
#         INSERT INTO "student_grade" (
#          
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''',(''))
cur.execute('DELETE FROM "Archive_data" WHERE "Name" = ? AND "Last_name" = ?', ('John', 'Doe'))

# conn.execute("PRAGMA foreign_keys = ON;")

# cur.execute('''
# INSERT INTO "student_grade" (
#      "name", "last_name", "math_score", "A_plus_score", 
#      "English_score", "Android_score", "python_score", 
#      "Django_score", "Sql_score", "server_score", "linux_score"
# ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', (
#      "John","Doe","good","good","good","good","godd","good","good","good","good"
# ))

# # Create the Archive_data table
# cur.execute('''
# CREATE TABLE "Archive_data" (
#     "Name" TEXT,
#     "Last_name" TEXT,
#     "Mother_name" TEXT,
#     "Father_name" TEXT,
#     "Email" TEXT,
#     "Phone_number" TEXT,
#     "Country" TEXT,
#     "City" TEXT,
#     "Age" TEXT,
#     "Native_language" TEXT,
#     "Health" TEXT,
#     "Gender" TEXT,
#     "Study" TEXT,
#     "Birthday" TEXT,
#     "Martial_status" TEXT,
#     "Image_data" TEXT
# )
# ''')

# # Create the student_grade table with foreign key
# cur.execute('''
# CREATE TABLE "student_grade" (
#     "name" TEXT,
#     "last_name" TEXT,
#     "math_score" TEXT,
#     "A_plus_score" TEXT,
#     "English_score" TEXT,
#     "Android_score" TEXT,
#     "python_score" TEXT,
#     "Django_score" TEXT,
#     "Sql_score" TEXT,
#     "server_score" TEXT,
#     "linux_score" TEXT,
#     FOREIGN KEY ("name", "last_name") REFERENCES "Archive_data" ("Name", "Last_name") ON DELETE CASCADE
# )
# ''')

# Add a new record to Archive_data
# cur.execute('''
# INSERT INTO "Archive_data" (
#     "Name", "Last_name", "Mother_name", "Father_name", "Email", 
#     "Phone_number", "Country", "City", "Age", "Native_language", 
#     "Health", "Gender", "Study", "Birthday", "Martial_status", "Image_data"
# ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', (
#     'John', 'Doe', 'Jane Doe', 'Richard Doe', 'john.doe@example.com',
#     '1234567890', 'USA', 'New York', '30', 'English',
#     'Good', 'Male', 'Computer Science', '1993-01-01', 'Single', 'path/to/image.png'
# ))


# Commit the changes and close the connection
conn.commit()
conn.close()
