
# CodeAlpha Cybersecurity Internship — Task 3
## Secure Coding Review: SQL Injection Prevention

### 📌 Project Overview

This project demonstrates how SQL Injection vulnerabilities can occur in Python applications when user input is directly incorporated into SQL queries.

Using Python and SQLite, I developed two implementations:

- A vulnerable application that uses unsafe SQL query construction.
- A secure application that uses parameterized queries and input validation.

The project compares both implementations and uses automated unit testing to verify their behavior against SQL injection attempts.

### 🎯 Objectives

- Understand how SQL Injection vulnerabilities occur.
- Identify security risks in dynamically constructed SQL queries.
- Demonstrate a SQL injection attack in a controlled environment.
- Implement secure database query handling.
- Validate user input before processing database operations.
- Test and compare vulnerable and secure implementations.

### 🧰 Technologies Used

- **Python** — Application development and testing.
- **SQLite** — Database management.
- **SQL** — Database queries.
- **Python `unittest`** — Automated security testing.
- **Visual Studio Code** — Development environment.
  
 A Video Describing about the project.
- https://youtu.be/navFkUS0RLg


### 📂 Project Structure

```text
Secure_Coding_Review/
│
├── vulnerable_app.py
├── secure_app.py
├── test_security_review.py
└── README.md
```

### 🔍 1. Identifying the Vulnerability

The vulnerable implementation constructs SQL queries using direct string concatenation.

Example:

```python
query = (
    "SELECT * FROM students "
    + "WHERE username = '" + username + "'"
)

return connection.execute(query).fetchall()
```

This approach is unsafe because user input becomes part of the SQL command itself.

### ⚠️ 2. SQL Injection Demonstration

The following test payload was used in the controlled demonstration:

```text
' OR '1'='1
```

It changes the query condition so that it evaluates as true for all records.

As a result, the vulnerable implementation returns all four fictional student records instead of restricting the result to the requested username.

### 🔐 3. Secure Coding Implementation

The vulnerable query was replaced with a parameterized SQL query.

```python
query = """
    SELECT * FROM students
    WHERE username = ?
"""

return connection.execute(query, (username,)).fetchall()
```

The `?` placeholder separates the SQL statement from the supplied user input.

**Additional input validation includes:**

- Checking that the input is a string.
- Removing unnecessary leading and trailing whitespace using `.strip()`.
- Rejecting empty input.
- Rejecting input longer than 50 characters.

These measures improve input handling, while parameterized queries address the SQL injection risk demonstrated in this project.

### 🧪 4. Automated Security Testing

The project includes six automated tests using Python's `unittest` framework.

| Test Case | Expected Behavior |
|---|---|
| Normal search | Correct student record is returned |
| Vulnerable SQL injection | Demonstrates exposure of all four records |
| Secure SQL injection | Returns no matching record |
| Unknown username | Returns an empty result |
| Empty input | Raises `ValueError` |
| Excessively long input | Raises `ValueError` |

### ▶️ 5. How to Run the Project

**Step 1: Clone the repository**

```bash
git clone <your-repository-url>
```

**Step 2: Navigate to the project folder**

```bash
cd Secure_Coding_Review
```

**Step 3: Run the automated tests**

```bash
python -m unittest -v test_security_review
```

**Expected test summary:**

```text
Ran 6 tests

OK
```

A passing vulnerable SQL injection test means the vulnerability was successfully reproduced. A passing secure SQL injection test means the same payload did not expose the student records in the secure implementation.

### 📊 6. Key Findings

| Vulnerable Implementation | Secure Implementation |
|---|---|
| Uses string concatenation | Uses parameterized queries |
| User input becomes part of SQL syntax | User input is passed separately |
| Injection payload exposes all four records | The demonstrated payload returns no matching record |
| No input validation | Includes input validation |

### 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding SQL Injection vulnerabilities.
- Identifying insecure SQL query construction.
- Applying parameterized queries for safer database operations.
- Implementing basic input validation.
- Writing automated security tests.
- Comparing vulnerable and secure application behavior.
- Understanding the importance of secure coding practices.

### ⚠️ Disclaimer

This project is developed strictly for educational purposes in an isolated environment using fictional student data and an in-memory SQLite database. The vulnerability demonstration is not intended for use against real systems or unauthorized databases.

### 👩‍💻 Internship

**Organization:** CodeAlpha  
**Task:** Task 3 — Secure Coding Review  
**Domain:** Cybersecurity

