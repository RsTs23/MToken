from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from decouple import config
import mtoken
import os


application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return 'Unidentified API'

#Execute reward transfer of a certain amount to a wallet address  
class Form(Resource):
	
	def get(self, wallet_id, reward, api_key):
		#PRIVATE_KEY = os.environ['PRIVATE_KEY']
		#if PRIVATE_KEY != api_key:
		#	abort(403, message="Wrong API key")
		mtoken.transfer(wallet_id,reward)
		return jsonify(
				response_one = reward+" MToken  were awarded to the following wallet address: "+ wallet_id,
				status = "200"
			   )


		
api.add_resource(Form, "/form/<string:wallet_id>/<string:reward>")

if __name__ == "__main__":

	application.run()