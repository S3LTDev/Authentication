# oooo     oooo      o      ooooo  oooo   ooooooo   ooooooooooo ooooooooooo 
# 8888o   888      888       888  88   o88     888 88  888  88 88    888   
# 88 888o8 88     8  88        888           o888      888         888     
# 88  888  88    8oooo88      88 888      o888   o     888       888    oo 
# o88o  8  o88o o88o  o888o o88o  o888o o8888oooo88    o888o    o888oooo888                                                                         
# link  https://github.com/max2tz/Authentication
# author  max2tz https://github.com/max2tz
# license  GPL-3.0 License 

from flask import Flask, request
from flask_mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL Server
app.config['MYSQL_DATABASE_USER'] = 'USERNAME'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PASSWORD'
app.config['MYSQL_DATABASE_DB'] = 'DATABASE'
app.config['MYSQL_DATABASE_HOST'] = 'HOST'
mysql.init_app(app)

# Key Configuration
admin_key = "key"

# Check_HWID Route
@app.route('/check_hwid', methods=['POST'])
def check_hwid():
    hwid = request.json['hwid']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM hwid_table WHERE hwid={hwid}")
    data = cursor.fetchone()
    if data:
        return "", 200
    else:
        return "", 401

    cursor.close() 
    conn.close()

# Add_HWID Route
@app.route('/add_hwid', methods=['POST'])
def add_hwid():
    key = request.json['key']
    hwid = request.json['hwid']
    if (key == admin_key):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO hwid_table (hwid) VALUES ({hwid})")
        conn.commit()
        cursor.close() 
        conn.close()
        return "", 201
    else:
        return "", 401
    
# Remove_HWID Route
@app.route('/remove_hwid', methods=['POST'])
def add_hwid():
    key = request.json['key']
    hwid = request.json['hwid']
    if (key == admin_key):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM hwid_table WHERE hwid={hwid}")
        conn.commit()
        cursor.close() 
        conn.close()
        return "", 201
    else:
        return "", 401

if __name__ == '__main__':
    app.run(debug=True)