""" Implement a Singleton class Configuration that reads configuration settings from a file. Ensure only
one instance of Configuration exists and is used throughout the application. Add a method
get_setting to retrieve configuration values. Demonstrate accessing configuration settings.
Concepts Covered: Singleton Pattern with Configuration """

import json

class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def load_settings(self, filename):
        with open(filename, 'r') as file:
            self.settings = json.load(file)

    def get_setting(self, key):
        return self.settings.get(key)

config = Configuration()
config.load_settings('config.json')

print("Database Host:", config.get_setting('database_host'))
print("API Key:", config.get_setting('api_key'))

another_config = Configuration()
print("Is the same instance:", config is another_config)


"""
{
    "database_host": "localhost",
    "api_key": "your_api_key_here"
}
"""
