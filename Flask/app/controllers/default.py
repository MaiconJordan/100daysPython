from app import app

@app.route("/")
def inde():
    return "Hello World!" 