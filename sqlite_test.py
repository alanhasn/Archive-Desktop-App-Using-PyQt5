import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('mydatabase2.db')

# Create a cursor object
cursor = conn.cursor()

# Create the users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
""")

# Create the posts table with a foreign key reference to the users table and ON DELETE CASCADE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
""")

# Insert some data into the users table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("John Doe", "johndoe@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Jane Smith", "janesmith@example.com"))

# Insert some data into the posts table
cursor.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", ("My First Post", "This is the content of my first post.", 1))
cursor.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", ("Another Post", "This is the content of another post.", 1))
cursor.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", ("Jane's Post", "This is Jane's post.", 2))

# Delete a user and observe the cascade effect
cursor.execute("DELETE FROM users WHERE id = 1")

# Commit the changes and close the connection
conn.commit()
conn.close()