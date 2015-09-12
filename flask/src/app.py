from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "I'am online! :D"

@app.route("/about")
def about():
    return "About page ;D"

@app.route("/contacts")
def contacts():
  return "Contacts Page"

@app.route("/seminars")
def seminars():
  return "Seminar web page"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')