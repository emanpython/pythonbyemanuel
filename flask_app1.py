import flask
app = Flask(__name__)

#Setup '/' as index
@app.route('/'):
def index():
	#send string to browser
	return 'Hello!!'

#run the app
if __name__ == "__main__":
	app.run()