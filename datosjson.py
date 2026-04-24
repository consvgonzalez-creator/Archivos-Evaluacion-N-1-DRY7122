import json 
with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)
print("ourjson")
print("Token: " + ourjson['access_token'])
print("Expira en: " + str(ourjson['expires_in']))

