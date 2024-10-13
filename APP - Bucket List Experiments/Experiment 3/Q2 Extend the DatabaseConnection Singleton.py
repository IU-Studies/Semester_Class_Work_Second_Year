""" Extend the DatabaseConnection Singleton class to include a method connect that prints a
connection message. Demonstrate that only one instance is used even when calling connect from
different parts of the program.
Concepts Covered: Singleton Pattern with Methods """

class DatabaseConnection:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def connect(self):
        return "Database connection established"

    @classmethod
    def get_instance(cls):
        return cls()

def connect_to_database():
    db = DatabaseConnection.get_instance()
    print(db.connect())  

def another_function():
    db = DatabaseConnection.get_instance()
    print(db.connect())  

connect_to_database()  
another_function()      

db1 = DatabaseConnection.get_instance()
db2 = DatabaseConnection.get_instance()
print(db1 is db2)      
