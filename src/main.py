from flask import Flask
from flask_restful import Resource, Api
from read_csv import *



app = Flask(__name__)
api = Api(app)


@app.route('/<id_str>', methods = ['GET'])
def api_users(id_str):
     id = str(id_str)
     try:
        json_data = bigdata.get_id(id)
        return json_data
     except:
         return 'Error 404 ID not found'



if __name__ == '__main__':

     print('Getting data from sources')
     bigdata = MergeData()
     print ('Done')
     app.run(port=5002)


