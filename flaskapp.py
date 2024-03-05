from flask import Flask, redirect, url_for, render_template, request, SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", content=["tim", "joe", "jon"])

if __name__ == "__main__":
    app.run()