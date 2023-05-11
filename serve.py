from flask import Flask, redirect, url_for, request
import socket
import subprocess


app = Flask(__name__)

seed = [0]


# Do intensive computation to stress the CPU


@app.route('/', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        data = request.get_json()
        seed[0] = data['num']
        s = subprocess.run(["python", "/content/drive/My Drive/Colab Notebooks/stress_cpu.py"], capture_output=True, text=True)
        return ""
    elif request.method == 'GET':
        private_ip = socket.gethostname()
        return str(private_ip)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8800)

##  curl -X GET  http://localhost:8800
##  curl -H "content-Type: application/json" -X POST -d '{"num":200}' http://localhost:8800
##  curl -X GET  update-683731185.us-west-2.elb.amazonaws.com
##  curl -H "content-Type: application/json" -X POST -d '{"num":200}' update-683731185.us-west-2.elb.amazonaws.com


