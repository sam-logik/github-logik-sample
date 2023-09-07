import http.client 
 from codecs import encode 
 import mimetypes 
 import requests 
 import http.client 
 import json 
  
  
 def main(): 
     access_token = authenticate() 
     jwt = get_jwt(access_token) 
     upload_file(jwt) 
  
  
 def upload_file(jwt): 
     conn = http.client.HTTPSConnection("logiksdo.demo01.logik.io") 
     dataList = [] 
     boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T' 
     dataList.append(encode('--' + boundary)) 
     dataList.append(encode( 
         'Content-Disposition: form-data; name=file; filename={0}'.format('Archive.zip'))) 
  
     fileType = mimetypes.guess_type( 
         './Archive.zip')[0] or 'application/octet-stream' 
     dataList.append(encode('Content-Type: {}'.format(fileType))) 
     dataList.append(encode('')) 
  
     with open('./Archive.zip', 'rb') as f: 
         dataList.append(f.read()) 
     dataList.append(encode('--'+boundary+'--')) 
     dataList.append(encode('')) 
     body = b'\r\n'.join(dataList) 
     payload = body 
     headers = { 
         'Authorization': 'Bearer ' + jwt, 
         'Cookie': 'SESSION=b5e317e6-fd77-4ba1-8fdf-95c0ff9fa4f8', 
         'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
     } 
     conn.request("POST", "/api/admin/v2/uploadFile", payload, headers) 
     res = conn.getresponse() 
     data = res.read() 
     print(json.loads(data.decode("utf-8"))) 
  
  
 def get_jwt(access_token): 
     conn = http.client.HTTPSConnection("cl1678124019990.my.salesforce.com") 
     payload = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Aaccess_token&subject_token=' + access_token 
     headers = { 
         'Content-Type': 'application/x-www-form-urlencoded', 
         'Authorization': 'Bearer ' + access_token, 
         'Cookie': 'BrowserId=QVUsJeUYEe2p-5XkE8VKjA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1' 
     } 
     conn.request("POST", "/services/oauth2/token", payload, headers) 
     res = conn.getresponse() 
     data = res.read() 
     print(data.decode("utf-8")) 
     return json.loads(data.decode("utf-8"))["access_token"] 
  
  
 def authenticate(): 
     conn = http.client.HTTPSConnection("cl1678124019990.my.salesforce.com") 
     payload = '' 
     headers = { 
         'Cookie': 'BrowserId=QVUsJeUYEe2p-5XkE8VKjA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1' 
     } 
     conn.request("POST", "/services/oauth2/token?username=logik_sdo@demo-logik.com&password=PASSWORD&grant_type=password&client_id=3MVG9X12xD2kqQmZIFg8mJZEAnR7NjO_PLhWRylHOfqnZ82i9FkzbNOPZOlN4_CZw7rgw32H_J1UZOF3xlZRS&client_secret=secret", payload, headers) 
     res = conn.getresponse() 
     data = res.read() 
     print(json.loads(data.decode("utf-8"))) 
     return json.loads(data.decode("utf-8"))["access_token"] 
  
  
 if __name__ == "__main__": 
     main()
