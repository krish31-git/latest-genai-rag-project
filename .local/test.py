import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    
  "question": "How can I request a refill for my prescription at Lamna Healthcare?",
  "chat_history": []


}

body = str.encode(json.dumps(data))

url = 'https://rag-genaiops-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1jN2wzSXo5M2c3dXdnTmVFbW13X1dZR1BrbyIsImtpZCI6Ik1jN2wzSXo5M2c3dXdnTmVFbW13X1dZR1BrbyJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2FmYTY4OTlkLWFhNDYtNDk5Mi1hM2ViLTVjODAxNWFhNWQxZi8iLCJpYXQiOjE3Mjg2ODIxMjgsIm5iZiI6MTcyODY4MjEyOCwiZXhwIjoxNzI4Njg2NjM2LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFlBQUFBSy9Fb21aN3VnNTRzUzRuNW9WejZWbW1xaHpSV1JISi9Kc29YeFhVTTNUNUpmeGVWNWdNem1TOXlVS3lUV1dTcUduRlZ3cSs0V3dRTlU3enBjaGcrV3B2eTRnRXZyZlppWDR5Ui84T2tFeW89IiwiYW1yIjpbInB3ZCIsInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiMGE3NTIwYjMtNDU3YS00NDEzLTg3YTUtNWI0OTVmNjQ0YTY3IiwiZmFtaWx5X25hbWUiOiJBZG1pbmlzdHJhdG9yIiwiZ2l2ZW5fbmFtZSI6IlN5c3RlbSIsImdyb3VwcyI6WyI5Nzc5YzUyOC0wZWM3LTQ5M2EtYWY2NS1kNTQ5MjlmNGZiZjQiLCJjOTA4MzczNC1hYzA0LTRmOTctOWQ2Yy0zMDEyZjJhMjhhMTgiLCI4ZjlmNjI1Ny1jMTFjLTQyMWMtYTI4OS02ZTU1ZjM3N2E4ODYiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMjYwMDoxNzAwOjZlMTo1N2QwOmQxNzU6YWQ1Nzo5Y2RmOmQ4M2UiLCJuYW1lIjoiU3lzdGVtIEFkbWluaXN0cmF0b3IiLCJvaWQiOiJjOTk2ZWFiZC0yYmJiLTQwNTEtYjM0MS0yNTZhOWYwZTQwMDEiLCJwdWlkIjoiMTAwMzIwMDM5RjczQzhGRiIsInJoIjoiMC5BYjBBblltbXIwYXFra21qNjF5QUZhcGRIMTl2cGhqZjJ4ZE1uZGNXTkhFcW5MNERBZWsuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiU0otalppYTBaV0JLUXotRW9sUl8xNTN6ckxBNkxQUkFvdFM4WVJzelV6RSIsInRpZCI6ImFmYTY4OTlkLWFhNDYtNDk5Mi1hM2ViLTVjODAxNWFhNWQxZiIsInVuaXF1ZV9uYW1lIjoiYWRtaW5ATW5nRW52TUNBUDkyNzI1NS5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJhZG1pbkBNbmdFbnZNQ0FQOTI3MjU1Lm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6IjBJdU1zbE1jVUV5RndrZG9NNE1LQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiIxIDQifQ.PlldAzghIs-ImkUYaHkYZitF4KDMwelaSCZdPgJS0LYG_7nHtTBzYOfeOgKJSpLwL630LS2ninzHRZemwbgKwquJa3F2Gf_UGkUk5dXoL7DBIomcT7pUGkvvk8h30p3X3mYmv0mvM4nCPYCd44UYXCeA1kGS3twp8A3zaUDAF2SOi5M050nu9lQWQ7OR5muqyD9sMsdanGf3Jqq8xPaZiKxzfiZchRPJjCT8zOekq-Tbhb8PqImGYr0yEsOnVyX4kcJeAI2MIFqUW6_jpJBNem-8DRWBm-WVmega_I8c7cRnekjZbKv1vLG_jkwJin25lrWAPdlX_ZkbfgDo0E9VQA'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))