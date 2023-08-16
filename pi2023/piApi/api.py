from flask import Flask,request
from utils import rc,changeContent
from json import dumps

app=Flask(__name__)
app.secret_key='myP4330rd'


@app.route('/')
def index():
	return rc()

@app.route('/changeData', methods=['POST'])
def changeMain():
	try:
		changeContent(dumps(request.form['mainContent']))

	except:
		return 'Dont saved!'
	else:
		return 'saved!'


if __name__=='__main__':
	host='127.1.0.0'
	port=12001
	print(f'server running in {host}:{port}')
	app.run(host,port,True)
