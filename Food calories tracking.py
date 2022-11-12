from flask import Flask,render_template,request,redirect,jsonify
#from datetime import datetime
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

# Connect to  mongoDB Database
try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    client.server_info()
    db = client['users']
    collections = db['userscollection']
except:
    print("Error Cannot Connect to MongoDB")

# Get method to response the courses as a json type
@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add_page():

    if request.method=='POST':
        
        date1=request.form['date']
        item=request.form['food']
        fat=float(request.form['fat'])
        protein=float(request.form['protein'])
        carbo=float(request.form['carbo'])
        calorie=4*carbo+4*protein+9*fat
        mydict={"food":item,'fat':fat,'protein':protein,'carbo':carbo,'calorie':calorie,'date':date1}
        collections.insert_one(mydict)
        return redirect('/home')
        
    return render_template('add.html')

@app.route('/home',methods=['GET','POST'])

def home_page():

    if request.method=='POST':
        date1=request.form['date']
        item=collections.find({'date':date1},{'date':1,'food':1,'fat':1,
        'protein':1,'calorie':1})
        return render_template('home.html',foods=item)
    
    item=collections.find()
    return render_template('home.html',foods=item)

@app.route('/home/<string:date>',methods=['GET'])
def home_page1(date):
    item=collections.find({'date':date})
    return render_template('home.html',foods=item)

@app.route('/home/<string:date>',methods=['DELETE'])
def delete(date):
    collections.delete_many({'date':date})
    return jsonify({'result':'True'})

if __name__=='__main__':
    app.run(debug=True,port=7000)