from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from flask and CICD newwwww '

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
#     app.run(ssl_context=('cert.pem', 'key.pem'))
#from flask import Flask
#import pymysql

#app = Flask(__name__)

#@app.route('/')
#def get_data():
    # Connect to MySQL database
    #db =pymysql.connect(
     #   host='10.0.134.249',
     #   user='public',
     #   password='Admin@123',
     #   database='public_db'
   # )

    # Execute SQL query
   # cursor = db.cursor()
    #cursor.execute("SELECT * FROM public_tb")

    # Fetch results
   # results = cursor.fetchall()

    # Close database connection
   # cursor.close()
  #  db.close()

    # Return results as a response
 #   return str(results)

#if __name__ == '__main__':
 #   app.run(host='0.0.0.0', port=8000, debug=True)
