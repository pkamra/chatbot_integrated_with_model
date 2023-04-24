try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from io import BytesIO
import json
import sys, os, base64, datetime, hashlib, hmac
from chalice import Chalice
from chalice import NotFoundError, BadRequestError

import sys, os, base64, datetime, hashlib, hmac

app = Chalice(app_name='logisticregression-analysis-api')
app.debug = True

import boto3

sagemaker = boto3.client('sagemaker-runtime')


@app.route('/', methods=['POST'], content_types=['application/json'], cors=True)
def handle_data():
    # Get the json from the request
    input_json = app.current_request.json_body['input']
    result = {'input': input_json}
    result = json.dumps(result)
    print("Data is :: ")
    print(result)
    # Send everything to the Sagemaker endpoint
    res = sagemaker.invoke_endpoint(
        EndpointName='logistic-demo-endpoint',
        Body=result,
        ContentType='application/json',
        Accept='application/json'
    )
    print(res)
    return res['Body'].read().decode('utf-8')
