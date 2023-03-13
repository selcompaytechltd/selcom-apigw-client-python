import requests;
import datetime
import base64
import hashlib
import hmac

class Client:
    def __init__(self,baseUrl, apiKey, apiSecret):
        self.baseUrl = baseUrl
        self.apiKey = apiKey
        self.apiSecret = apiSecret
         
    def computeHeader(self, dictData):
        apiKey_bytes = self.apiKey.encode('ascii')
        base64_bytes = base64.b64encode(apiKey_bytes)
        base64_apiKey= base64_bytes.decode('ascii')
        authToken = 'SELCOM '+ base64_apiKey

        now = datetime.datetime.now().astimezone()
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%S%z")

        signedFields = ""
        data= "timestamp=" + timestamp
        for  key in dictData:
            data  = data + "&" + key + "=" + str(dictData[key])
            if (signedFields == ''):
                signedFields = signedFields + key
            else:
                signedFields = signedFields + "," + key

        signature = hmac.new(
            key=bytes(str(self.apiSecret), 'utf-8'),
            msg=bytes(data, 'utf-8'),
            digestmod=hashlib.sha256).digest()
        digestBytes = base64.b64encode(signature)
        digest = digestBytes.decode('utf-8')
     

        return authToken, timestamp, digest, signedFields

    def postFunc(self, path, dictData):
        authToken, timestamp, digest, signedFields = self.computeHeader(dictData)
        url = self.baseUrl + path
        data = dictData
        
        headers = {
            "Content-type": "application/json",
                    "Authorization":authToken,
                    "Digest-Method": "HS256",
                    "Digest": digest,
                    "Timestamp": timestamp,
                    "Signed-Fields":signedFields}
        
        response=requests.post(url, json=data, headers=headers)
        

        return response.json()

    def getFunc(self,path, dictData):
        authToken, timestamp, digest, signedFields = self.computeHeader(dictData)
        url = self.baseUrl + path
        params = dictData
        
        headers = {
            "Content-type": "application/json",
                    "Authorization":authToken,
                    "Digest-Method": "HS256",
                    "Digest": digest,
                    "Timestamp": timestamp,
                    "Signed-Fields":signedFields}
        
        response=requests.get(url, params=params, headers=headers)

        return response.json()

    def deleteFunc(self,path, dictData):
        authToken, timestamp, digest, signedFields = self.computeHeader(dictData)
        url = self.baseUrl + path

        params = dictData
        
        headers = {
            "Content-type": "application/json",
                    "Authorization":authToken,
                    "Digest-Method": "HS256",
                    "Digest": digest,
                    "Timestamp": timestamp,
                    "Signed-Fields":signedFields}
        
        response=requests.delete(url, params=params, headers=headers)

        return response.json()

