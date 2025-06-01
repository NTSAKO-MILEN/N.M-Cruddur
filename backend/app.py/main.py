from flask import Flask
import os
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='Cruddur', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)

@app.route('/')
def home():
    return "Hello, Backend!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


  
