from flask import Flask , render_template,request,redirect,url_for  
import pymysql as sql
app = Flask(__name__)
conn = sql.connect(host='localhost',user='root',passwd='',db='studentdb')
print(conn)
@app.route("/")
def showData():
    if(conn) : 
         cur = conn.cursor()
         cur.execute("SELECT * FROM `student` WHERE 1")
         rows = cur.fetchall()
         return render_template('index.html',data=rows)

@app.route("/student")
def showForm():
         return render_template('addstudent.html')

@app.route("/insert",methods=['POST'])
def insert():
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql = "Insert into `student` (`fname`,`lname`,`phone`) values(%s,%s,%s)"
            cursor.execute(sql,(fname,lname,phone))
            conn.commit()
        return redirect(url_for('showData'))
if __name__ == "__main__":
    app.run(debug=True)
    
