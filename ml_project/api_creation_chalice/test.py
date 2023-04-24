import requests
import json
# Define test JSON
input_sentiment = '{"input": "this account is more passive than my other accounts"}'
input_json = json.dumps({'input':'this account is more passive than my other accounts'})
print(input_json)
# Define your api URL here
api_url = 'https://483cyfpx39.execute-api.us-east-1.amazonaws.com/api/'
res = requests.post(api_url,json=input_json)
output_api = res.text
print(output_api)

