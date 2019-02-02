import requests

url = "https://gateway.test.nab.com.au/api/rest/version/46/merchant/TESTVICTESNB237/session"

payload = "{\n    \"lineOfBusiness\": \"test_socks\"\n}"
headers = {
    'Authorization': "Basic ",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, auth=('merchant.TESTVICTESNB237','ed17a6e2ed43172c0f7bde912cbe54de'), data=payload, headers=headers)

print(response.text)