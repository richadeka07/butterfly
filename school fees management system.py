import sqlite3

class SchoolFeesManager:
    def __init__(self, db_name="school_fees.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade TEXT NOT NULL,
                total_fee REAL NOT NULL,
                paid_fee REAL DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_student(self, name, grade, total_fee):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO students (name, grade, total_fee) VALUES (?, ?, ?)", (name, grade, total_fee))
        self.conn.commit()

    def record_payment(self, student_id, amount):
        cur = self.conn.cursor()
        cur.execute("UPDATE students SET paid_fee = paid_fee + ? WHERE id = ?", (amount, student_id))
        self.conn.commit()

    def get_balance(self, student_id):
        cur = self.conn.cursor()
        cur.execute("SELECT total_fee, paid_fee FROM students WHERE id = ?", (student_id,))
        row = cur.fetchone()
        if row:
            return row[0] - row[1]
        return None

    def list_students(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, grade, total_fee, paid_fee FROM students")
        return cur.fetchall()

    def close(self):
        self.conn.close()
'''
# Example usage:
if __name__ == "__main__":
    manager = SchoolFeesManager()
    manager.add_student("Alice", "Grade 1", 5000)
    manager.add_student("Bob", "Grade 2", 6000)
    manager.record_payment(1, 2000)
    print("Student balances:")
    for student in manager.list_students():
        print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Total Fee: {student[3]}, Paid: {student[4]}, Balance: {student[3]-student[4]}")
    manager.close()
'''