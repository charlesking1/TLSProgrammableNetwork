#!/usr/bin/python3
#

import requests

import getpass
import sys
import json

account = input("Enter your account details 240262029704: ")
mypassword = getpass.getpass()

#print("\n","Account: ", account)
#print("password: ", mypassword)

# Define headers in a Dictionary type
headers = {
    'Accepts': 'application/json',
#    'Accept-Charset': 'UTF-8',
}

# Define data in a List type
data = [
  ('grant_type', 'password'),
  ('username', '240262029704/charles.king.customer'),
  ('password', mypassword),
]

# TPN Auth URL
auth_url = 'https://penapi.pacnetconnect.com/1.0.0/auth/generatetoken'
validate_url = 'https://penapi.pacnetconnect.com/1.0.0/auth/validatetoken'

auth_response = requests.post(auth_url, headers=headers, data=data)


# For successful API call, response code will be 200 (OK)
if (auth_response.ok):

# Decode bytes type (e.g. b'{blah}') output into a str.
# json.loads needs str not bytes
    dec_auth = auth_response.content.decode('UTF-8')
    
#    print("Decode Auth: ", dec_auth)
#    print("\n")

# Loading the response data into a dict variable
# json.loads takes in only binary or string variables so using content to fetch binary content
# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jauthData = json.loads(dec_auth)


## Can run other queries from here, once have "access_token" for Bearer ID

    valid_headers = {
        'Authorization': 'Bearer  ' + jauthData["access_token"],
        'Content-Type': 'application/json',
    }

## Query 2 BillingID: - GET /1.0.0/auth/validatetoken
    validate_response = requests.get(validate_url, headers=valid_headers)

# For successful API call, response code will be 200 (OK)
    if (validate_response.ok):

# Decode bytes type (e.g. b'{blah}') output into a str.
# json.loads needs str not bytes
        dec_valid = validate_response.content.decode('UTF-8')

        jvalidData = json.loads(dec_valid)

# Troubleshooting
#        print("* The important Billing Account* : ", jvalidData["billings"])
#        print("\n")

        print("Company Name: ", jvalidData["company-name"], "\n")
#        print("Location: ", jvalidData["address"], " in Country: ", jvalidData[country], "\n")

# Troubleshooting
#        print("The response contains {0} properties".format(len(jvalidData)))
#        print("\n")

# Troubleshooting
# Output data from second Validation - Billing request - gives verbose output
#        for key in jvalidData:
#            print(" " + key + " : " + str(jvalidData[key]))

#        print("Exit inner loop\n")


# Output data from Billing Data stored in 'List' type var
# Inside this is a 'Dictionary' type var
# i.e.  [{'billing-account': '1221', 'billingid': 'a66cbb7f-0a9c-419c-9944-d7f887f9cac1'}]

        MyBillingData = jvalidData["billings"]
#        print(type(MyBillingData), "\n")
#        print(type(MyBillingData[0]), "\n")
#        print(" ", MyBillingData[0], "\n")

# Load first element of list into Dictionary
        MyBill_Dict = MyBillingData[0]
        print("Billing Account: ", MyBill_Dict["billing-account"], "\n")
        print("Billing ID: ", MyBill_Dict["billingid"], "\n")

# Output data from first Authentication request
    #for key in jauthData:
    #   print (" " + key + " : " + str(jauthData[key]))

    print("* The important access token* : ", jauthData["access_token"])
    print("\n")
#    print("The response contains {0} properties".format(len(jauthData)))
#    print("\n")


else:
# If response code is not ok (200), print the resulting http error code with description
#myResponse.raise_for_status()
    print(auth_response.status_code)
