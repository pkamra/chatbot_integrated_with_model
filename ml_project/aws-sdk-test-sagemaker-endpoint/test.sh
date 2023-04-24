#!/usr/bin/env bash
ENDPOINT_NAME=logistic-endpoint
aws sagemaker-runtime invoke-endpoint \
--endpoint-name ${ENDPOINT_NAME} \
--body '{"input":"this account is more passive than my other accounts"}' \
--content-type 'application/json' \
  prediction_response.json
cat prediction_response.json