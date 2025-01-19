from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
import ast

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class AppWindow(Screen):
    pass

class Main(MDApp):
    def build(self):
        # Return the loaded KV file which contains the UI
        return Builder.load_file("Registration.kv")

    def login(self, username, password):
        # Attempt to read the database
        try:
            with open("database.txt") as f:
                data = f.read()
                # Reconstruct the data as a dictionary
                database = ast.literal_eval(data)
        except FileNotFoundError:
            # If the file does not exist, create an empty database
            database = {}

        if username in database and database[username] == password:
            # If username exists and password matches
            self.root.current = "app"
        else:
            # If login fails, handle accordingly (e.g., display a message)
            print("Invalid username or password.")

    def sign_up(self, username, password):
        # Attempt to read the database
        try:
            with open("database.txt") as f:
                data = f.read()
                # Reconstruct the data as a dictionary
                database = ast.literal_eval(data)
        except FileNotFoundError:
            # If the file does not exist, create an empty database
            database = {}

        if username in database:
            # If username already exists
            print("Username already exists.")
        else:
            # If username is new, add it to the database
            database[username] = password

            # Save the updated database back to the file
            with open("database.txt", "w") as f:
                f.write(str(database))

            print("Account created successfully.")


if __name__ == "__main__":
    Main().run()
