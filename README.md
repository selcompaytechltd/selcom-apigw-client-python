 
<h1 align="center">SELCOM API ACCESS CLIENT</h1>

<p align='center'>

<img src="https://img.shields.io/pypi/pyversions/3">

</p >

## Homepage
https://developers.selcommobile.com/

## Description
This is a library containing functions that aid in the accessing of selcom api. IT is made up pf 4 functions.

## Installation 
pip install selcom_apigw_client

### Use

```py
# import apigwClient module
from selcom_apigw_client import apigwClient

# initalize a new CLient instace with values of the base url, api key and api secret
client = apigwClient.Client(baseUrl, apiKey, apiSecret)

#computeHeader  a dictionary/json containing data to bes submitted
#computeHeader returns a tuple with values for the following header fields: 
# Authorization, Timestamp, Digest, Signed-Fields
client.computeHeader( dictData)

#postFuct takes relative path to base url and dictionary containing data to be submitted 
#It performs a POST request of the submitted data to the destniation url generatingg the header internally
#IT returns a String containing the response to the request
client.postFunc(path, dictData)

#ggetFuct takestakes relative path to base url and dictionary containing data to be submitted 
#It performs a GET request adding the query to the  url and generatingg the header internally
#IT returns a String containing the response to the request
client.getFunc(path, dictData)

#deletetFuct takestakes relative path to base url and dictionarycontaining data of wuery 
#It performs a DELETE request adding the query to the  url and generatingg the header internally
#IT returns a String containing the response to the request
client.deleteFunc(path, dictData)
```

## Example 
```py


#import package
from selcom_apigw_client import apigwClient
# initalize a new apiAccess instace with values of the base url, api key and api secret

apiKey = '202cb962ac59075b964b07152d234b70'
apiSecret = '81dc9bdb52d04dc20036dbd8313ed055'
baseUrl = "http://example.com"


client = apigwClient.Client(baseUrl, apiKey, apiSecret)

#order data
orderDict = {
"vendor":"VENDORTILL",
"order_id":"1218d5Qb",
"buyer_email": "john@example.com",
"buyer_name": "John Joh",
"buyer_phone": "255682555555",
"amount":  8000,
"currency":"TZS",
"buyer_remarks":"None",
"merchant_remarks":"None",
"no_of_items":  1

}
#path relatiive to base url
orderPath = "/v1/checkout/create-order-minimal"
#crate new order

response = client.postFunc(orderPath, orderDict)

#get response data
print(response)
```