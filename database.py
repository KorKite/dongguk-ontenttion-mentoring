import pyrebase
import json
from datetime import datetime
import time
import asyncio



class Client:
    def __init__(self):
        """
        class: Initialize Database Client
        """
        with open("auth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def get_history(self, end_cls):
        history_list = []
        if end_cls:
            with open("history_save.txt", "r") as t:
                for i in t.readlines():
                    history_list.append(float(i))
        else:
            with open("history.txt", "r") as t:
                for i in t.readlines():
                    history_list.append(float(i))
        return history_list

    def get_att(self):
        read_data = dict(self.db.child("attention").get().val()).items()
        whole_data = [i[1] for i in read_data]
        return sorted(whole_data, key=lambda x:x["s_id"])

    def run(self):
        
        while True:
            print("⭐️ Generated")
            understand_score = 0
            read_data = dict(self.db.child("understand").get().val()).items()
            for i in read_data:
                understand_score += i[1]["understand"]

            understand_avg = understand_score/len(read_data)
            with open("history.txt", "a") as t:
                t.write(str(understand_avg)+"\n")
            
            time.sleep(30)
        
            





if __name__ == "__main__":
    # run()
    cl = Client()
    cl.run()
    # cl.get_att()
