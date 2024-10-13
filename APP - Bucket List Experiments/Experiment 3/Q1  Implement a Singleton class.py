""" Implement a Singleton class named DatabaseConnection that ensures only one instance of
the class can exist. Create a method get_instance that returns the single instance of the class.
Demonstrate that multiple calls to get_instance return the same instance.
Concepts Covered: Singleton Pattern """

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

db1 = DatabaseConnection.get_instance()
db2 = DatabaseConnection.get_instance()

print(db1.connect())  
print(db1 is db2)     
