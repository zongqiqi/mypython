import requests
import json


# url_token='https://api.shanbay.com/endpoint/'

# headers={
# 	'Authorization':'Bearer TOKEN'
# 	}

# params={
# 	'access_token':'TOKEN'
# 	}

# r=requests.get(url=url_token,headers=headers,params=params)

# print(r.text)

#授权
url_auth='https://api.shanbay.com/oauth2/authorize/'
param={
	'client_id':'9d29dc8486fe70877bf0',
	'response_type':'code',
	'state':'123'
}

r_auth=requests.get(url=url_auth,params=param)
print(r_auth.url)
print(r_auth.text)

