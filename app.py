from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://breq.dev/demos/vibrance/")


if __name__ == "__main__":
    app.run()
