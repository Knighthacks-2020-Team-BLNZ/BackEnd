import requests

url = "http://127.0.0.1:8000/looking/"

querystring = "user_type=2&user_subject=Physics&user_personality=ENFP&user_writeup=I+just+want+someone+to+teach+me+physids"
heads = {'content-type':'application/x-www-form-urlencoded'}

response = requests.request('POST',url, data=querystring, headers=heads)
print(response.content)

