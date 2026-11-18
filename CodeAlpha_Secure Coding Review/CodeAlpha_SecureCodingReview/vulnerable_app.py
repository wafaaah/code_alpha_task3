
import sqlite3


# ==========================================
# DATABASE SETUP
# ==========================================

def setup_database():

    connection = sqlite3.connect(":memory:")

    connection.execute("""
        CREATE TABLE students (
            username TEXT,
            full_name TEXT,
            email TEXT,
            department TEXT,
            phone TEXT,
            student_id TEXT,
            university TEXT,
            semester TEXT,
            cgpa TEXT,
            skills TEXT,
            address TEXT
        )
    """)

    # Insert four fictional student records
    connection.executemany(
        """
        INSERT INTO students VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """,
        [
            (
                "rumaisa",
                "Rumaisa Rahman",
                "rumaisa@example.com",
                "Computer Science",
                "01700000001",
                "CSE-101",
                "Demo University",
                "8th",
                "3.75",
                "Python, Django, SQL",
                "Dhaka, Bangladesh"
            ),
            (
                "waspia",
                "Waspia Rahman",
                "waspia@example.com",
                "Electrical Engineering",
                "01700000002",
                "EEE-102",
                "Demo University",
                "7th",
                "3.60",
                "Java, C++, Networking",
                "Chattogram, Bangladesh"
            ),
            (
                "sokina",
                "Sokina Khatun",
                "sokina@example.com",
                "Business Administration",
                "01700000003",
                "BBA-103",
                "Demo University",
                "6th",
                "3.85",
                "Marketing, Excel, Analytics",
                "Sylhet, Bangladesh"
            ),
            (
                "hasina",
                "Hasina Khatun",
                "hasina@example.com",
                "Computer Science",
                "01700000004",
                "CSE-104",
                "Demo University",
                "8th",
                "3.90",
                "Python, Machine Learning, AI",
                "Rajshahi, Bangladesh"
            )
        ]
    )

    return connection


# ==========================================
# VULNERABLE STUDENT SEARCH
# ==========================================

def find_student(connection, username):

    # SECURITY FLAW: SQL Injection
    query = (
        "SELECT * FROM students "
        + "WHERE username = '" + username + "'"
    )

    return connection.execute(query).fetchall()


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    db = setup_database()

    try:

        print("\n" + "=" * 55)
        print("       VULNERABLE STUDENT INFORMATION SYSTEM")
        print("=" * 55)

        username = input("\nEnter username: ")

        result = find_student(db, username)

        if result:

            print("\n===== STUDENT INFORMATION =====")

            columns = [
                "Username",
                "Full Name",
                "Email",
                "Department",
                "Phone",
                "Student ID",
                "University",
                "Semester",
                "CGPA",
                "Skills",
                "Address"
            ]

            for student in result:

                for column, value in zip(columns, student):
                    print(f"{column}: {value}")

                print("-" * 45)

        else:
            print("\nStudent not found.")

    except sqlite3.Error:
        print("\nDatabase error occurred.")

    finally:
        db.close()
