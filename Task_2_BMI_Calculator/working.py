import datetime
import sqlite3
conn = sqlite3.connect('bmi_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bmi_data
             (id INTEGER PRIMARY KEY, 
              name TEXT, 
              weight REAL, 
              height REAL, 
              bmi REAL, 
              date TEXT)''')
conn.commit()
def calculate_bmi(weight, height):
    return round(weight / (height/100)**2, 2)


def save_bmi_data(name, weight, height, bmi):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO bmi_data (name, weight, height, bmi, date) VALUES (?, ?, ?, ?, ?)",
              (name, weight, height, bmi, date))
    conn.commit()


def retrieve_data(name):
    c.execute("SELECT * FROM bmi_data WHERE name=?", (name,))
    return c.fetchall()