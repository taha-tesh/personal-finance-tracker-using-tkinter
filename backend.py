import sqlite3
from datetime import date
import csv

class IncertData:

    def __init__(self, user_name, descrepthion, amount, type):
        self.user_name = user_name
        self.descrepthion = descrepthion
        self.amount = amount
        self.type = type


    def SubmitData(self):

        conn = sqlite3.connect('data.db')

        create_table_query = '''CREATE TABLE IF NOT EXISTS users_data (user_name VARCHAR(100), description VARCHAR(1000), amount FLAOT, type VARCHAR(100))'''
        conn.execute(create_table_query)

        data_insert_query = '''INSERT INTO users_data VALUES (?, ?, ?, ?)'''
        data_insert_tupele = (self.user_name, self.descrepthion, self.amount, self.type)

        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tupele)

        conn.commit()
        conn.close()


class GetData:

    def __init__(self, user_name, type):
        self.user_name = user_name
        self.type = type

    def ReadData(self):

        conn = sqlite3.connect('data.db')

        if self.type == "Income":
        
            select_data_query = '''SELECT * FROM users_data WHERE type = ? AND user_name = ?'''
            select_data_tupele = (self.type, self.user_name)
        
            cursor = conn.cursor()
            cursor.execute(select_data_query, select_data_tupele)
            data = cursor.fetchall()
            print(data)
        
        elif self.type == "Expensis":

            select_data_query = '''SELECT * FROM users_data WHERE type = ? AND user_name = ?'''
            select_data_tupele = (self.type, self.user_name)
        
            cursor = conn.cursor()
            cursor.execute(select_data_query, select_data_tupele)
            data = cursor.fetchall()
            print(data)

        conn.commit()
        conn.close()

class Balance:

    def __init__(self, user_name, type):
        self.user_name = user_name
        self.type = type

    def CalculatBalace(self):

        conn = sqlite3.connect('data.db')

        type_1 = "Income"
        type_2 = "Expensis"
        
        select_data_query = '''SELECT SUM(amount) FROM users_data WHERE type = ? AND user_name = ?'''
        select_data_tupele = (type_1, self.user_name)
        
        cursor = conn.cursor()
        cursor.execute(select_data_query, select_data_tupele)
        income = cursor.fetchall()
        #print(income)
        select_data_query = '''SELECT SUM(amount) FROM users_data WHERE type = ? AND user_name = ?'''
        select_data_tupele = (type_2, self.user_name)
        
        cursor = conn.cursor()
        cursor.execute(select_data_query, select_data_tupele)
        expensis = cursor.fetchall()
        #print(expensis)
        if type(income[0][0]) == type(None):
            balance = "-" + str(expensis[0][0])
        elif type(expensis[0][0]) == type(None):
                balance = income[0][0]
        else:
            balance = income[0][0] - expensis[0][0]

        conn.commit()
        conn.close()

        return balance
    
class CalculateTotal:

    def __init__(self, user_name, type):
        self.user_name = user_name
        self.type = type

    def Calculate(self):

        conn = sqlite3.connect('data.db')
        
        select_data_query = '''SELECT SUM(amount) FROM users_data WHERE type = ? AND user_name = ?'''
        select_data_tupele = (self.type, self.user_name)
        
        cursor = conn.cursor()
        cursor.execute(select_data_query, select_data_tupele)
        total = cursor.fetchall()

        conn.commit()
        conn.close()

        return total[0][0]