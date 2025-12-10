from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_worl():
    return "Hello World"
@app.route("/about")
def about():
    return "Pagina sobre isso"

if __name__ == "__main__":
    app.run(debug=True)