import sqlite3

def create_table():
    conn = sqlite3.connect('Applicants.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Applicants(
            number TEXT PRIMARY KEY,
            name TEXT,
            gender TEXT,
            job_title TEXT,
            company TEXT,
            status TEXT,
            date_applied TEXT)''')
    conn.commit()
    conn.close()

def fetch_applicants():
    conn = sqlite3.connect('Applicants.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Applicants')
    applicants = cursor.fetchall()
    conn.close()
    return applicants

def insert_applicant(number, name, gender, job_title, company, status, date_applied):
    conn = sqlite3.connect('Applicants.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Applicants (number, name, gender, job_title, company, status, date_applied) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (number, name, gender, job_title, company, status, date_applied))
    conn.commit()
    conn.close()

def delete_applicant(number):
    conn = sqlite3.connect('Applicants.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Applicants WHERE number = ?', (number,))
    conn.commit()
    conn.close()

def update_applicant(name, gender, job_title, company, status, date_applied, number):
    conn = sqlite3.connect('Applicants.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE Applicants SET name = ?, gender = ?, job_title = ?, company = ?, status = ?, date_applied = ? WHERE number = ?''',
                   (name, gender, job_title, company, status, date_applied, number))
    conn.commit()
    conn.close()

def number_exists(number):
    conn = sqlite3.connect('Applicants.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Applicants WHERE number = ?', (number,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()
