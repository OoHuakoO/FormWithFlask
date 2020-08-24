from flask import Flask , render_template
import pymysql
app = Flask(__name__)
con = pymysql.connect('localhost','root','','studentdb')
@app.route("/")
def hello():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchAll()
        return render_template('index.html',data=age)

if __name__ == "__main__":
    app.run(debug=True)

