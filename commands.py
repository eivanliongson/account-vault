import sqlite3
from generate import Key

# hope someone could help me improve this

class Commands:
    def __init__(self):
        self.hold = ["Platform: ", "Username: ", "Password: "]
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        print("Connected! Hi there!")

    def create(self): # creates the table accounts
        try:
            self.conn.execute(""" 
            CREATE TABLE accounts(
                platform text,
                username text,
                password text
            )
            """)
        except: return 0


    def add_account(self): # add account to the database
        trig = Key()
        platform = input("\nEnter Platform: ").upper()
        username = input("Enter Username: ")
        print("GENERATE new PASSWORD or USE your own PASSWORD?")
        ans = input("GENERATE or USE: ").upper()
        if ans == "GENERATE":
            password = trig.generate()
        elif ans == "USE":
            password = input("Enter password: ")
        

        # sqlite command
        with self.conn:
            self.c.execute("insert into accounts values (:platform, :username, :password)", 
            {"platform": platform, "username": username, "password": password})
            # dictionary key => value
            self.conn.commit()
            print("*"*5)
            print ("\nSuccess!")

    def get_all_accounts(self):
        with self.conn:
            data = self.c.execute("select * from accounts").fetchall()
            print("\nAccounts registered: \n")
            for i in range(len(data)):
                print(data[i])
                

    def get_account(self, platform):
        get = platform
        with self.conn:
            data = self.c.execute("select * from accounts where platform = :platform", 
            {"platform": get.upper()}).fetchone()
            # display data
            print("\n"*3 + "Acoount Info: ")
            for i in range(len(data)):
                print(self.hold[i] + data[i])


    def list_all_platforms(self):
        with self.conn:
            data = self.c.execute("select platform from accounts").fetchall()
            print("\nPlatform Used: \n")
            for i in range(len(data)):
                print(data[i][0])
