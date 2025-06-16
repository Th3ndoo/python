# get the country code fro the dictionary

country_code = {"South Africa":"0027",
                "USA":"001",
                "Nepal":'0097',}

print("the country code for South Africa")
print(country_code.get("South Africa","not found"))

print("the country code  for Nigeria")
print(country_code.get("Nigeria","not found"))