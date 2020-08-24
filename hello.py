from flask import Flask , render_template
import pymysql as sql
app = Flask(__name__)
conn = sql.connect(host='localhost',user='root',passwd='',db='studentdb')
print(conn)
@app.route("/")
def hello():
      with conn:
         cur = conn.cursor()
         cur.execute("select * from student WHERE 1")
         rows = cur.fetchall()
         return render_template('index.html',data=rows)

if __name__ == "__main__":
    app.run(debug=True)

