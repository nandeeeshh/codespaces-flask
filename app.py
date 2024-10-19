from flask import Flask, render_template
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route("/S")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/")
def htop():

    full_name = "Nandeesh P Math"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    ist = pytz.timezone("Asia/Kolkata")
    server_time_ist = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -bn1 | head -10")

    return render_template(
        "htop.html", 
        full_name=full_name, 
        username=username, 
        server_time=server_time_ist, 
        top_output=top_output
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)