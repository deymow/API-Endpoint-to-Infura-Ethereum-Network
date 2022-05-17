import requests
from flask import Flask

#Init app
app = Flask(__name__)

API_ENDPOINT = "https://mainnet.infura.io/v3/019d708205004cddb4abf1bdd2f4bcae"

#route
@app.route("/")
def hello():
	headers = {
		"Content-Type": "application/json"
	}
	data = "{\"jsonrpc\":\"2.0\",\"method\":\"eth_getBlockByNumber\",\"params\":[\"latest\",true], \"id\":1}" #serialization of my data sent over HTTP request

	response = requests.post(url = API_ENDPOINT, data = data, headers = headers) #posting of request to endpoints
	
	return response.json()	

	
if __name__ == "__main__":
	app.run (debug=True,host='0.0.0.0')