import requests

url = "https://twinword-word-associations-v1.p.rapidapi.com/associations/"

querystring = {"entry":"honest"}

headers = {
    'x-rapidapi-host': "twinword-word-associations-v1.p.rapidapi.com",
    'x-rapidapi-key': "2d880394dfmsh177cb8bde63f6e3p15ed44jsnf2caf75f146b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

listOfWords = response.text.partition("associations\":\"")[2].partition("\",\"associations_array")[0].split(", ")
print(listOfWords)
