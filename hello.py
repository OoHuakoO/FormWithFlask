from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    age = "python"
    return render_template('index.html',data=age)

if __name__ == "__main__":
    app.run(debug=True)

