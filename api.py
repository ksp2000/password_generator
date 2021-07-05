from flask import Flask, jsonify
from utils import password_generator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

@app.route('/v1/password/<int:length>', methods=['GET'])
def get_password(length):
    if length<8:
        return jsonify({'status':'failed','message':'Enter number greater than 8 to get secure password!'})
    else:
        password = password_generator(length)
        return jsonify({'status':'success','message':'Secure password generated!','length':length,'password':password})

if __name__ == '__main__':
    app.run(debug=True)