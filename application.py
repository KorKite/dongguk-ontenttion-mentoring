from flask import Flask, url_for, flash ,redirect, render_template, request, abort, json
from database import Client
import os
import sys
import threading


application = Flask(__name__)
client = Client()
END_CLS = True

@application.route("/")
def index():
    global END_CLS
    history = client.get_history(end_cls = END_CLS)
    labels = [f"{i//2}분 {30*(i%2)}초" for i in range(0, len(history))]
    return render_template("index.html", history=history, labels=labels, END_CLS=END_CLS)

@application.route("/attention")
def att():
    global END_CLS
    att = client.get_att()
    return render_template("att.html", att=att, END_CLS=END_CLS)

@application.route("/start_class")
def start_class():
    global END_CLS
    with open("history.txt", "w") as f:
        f.write("")
    END_CLS = False

    return redirect(url_for('index'))

@application.route("/end_class")
def end_class():
    global END_CLS
    END_CLS = True
    os.system("cp -f history.txt history_save.txt")
    return redirect(url_for('index'))


if __name__ == "__main__":
    print("\n✅ Server Run - https://onttention.run.goorm.io/ \n")
    application.run(host='0.0.0.0', port=5500, debug=True)
