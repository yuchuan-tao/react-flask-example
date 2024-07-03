from flask import Flask

app = Flask(__name__)

# Data API route
@app.route("/data")
def getData():
    return { "data": [[5.1, 3.5, 1.4, 0.2, "Iris-setosa"], [4.9, 3, 1.4, 0.2, "Iris-setosa"], [4.7, 3.2, 1.3, 0.2, "Iris-setosa"], [4.6, 3.1, 1.5, 0.2, "Iris-setosa"]] }

if __name__ == "__main__":
    app.run(debug=True)