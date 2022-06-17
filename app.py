from flask import Flask


app = Flask(__name__)

# API가 있어야 한다.
@app.route('/', methods = ['GET'])
def hello_world() :
    return 'Hello World hihihi'



if __name__ == '__main__' :
    app.run()