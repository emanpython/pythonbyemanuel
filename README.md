# pythonbyemanuel

Flask App - Basic login

Before you begin ensure you follow the following instructions

	1. pip3 install flask
	2. pip3 install flask_sqlalchemy

Ensure the install process went smoothly by running this command at the prompt:

	pip3 freeze

You should see "flask....=...."

Go to the Python shell, type: import flask

If it all went well, Flask is now installed on your sytem.

Note: It is generally good practise to develop your projects in virtual environments, enforces seperation from 
other projects on your system and their dependencies.

Your first flask app:

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

Save the file as first.py and Run it

Open an internet browser and enter the url: http://127.0.0.1:5000

The app will use HTTP port 5000, unless you reconfigure it.