
import json
import requests



baseUrl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"

#Spoof User-Agent to bypass restrictions
headers_dict = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}


#Main interface for Pincode and Date input
def main():


    print("###########################################")
    print("#        CoWin Availablity Bot            #")
    print("###########################################")
    
    #Get form url with PINCODE && DATE inputs from user
    pincode = input("Enter pincode: ")
    date = input("Enter date: ")
    url = baseUrl + "pincode=" + pincode + "&date=" + date

    response = requests.get(url, headers=headers_dict)

    #check for OK status
    if response.status_code == 200:

        jsonStr = json.loads(response.text)
        center_list = list(jsonStr['centers'])
        valid_centers = availCenter(center_list)

        #output available centers
        if len(valid_centers) > 0:

            print("######################################")
            print("#        Available Centers           #")
            print("######################################")
            
            print(valid_centers)
            
        else:

            print("No center available")
    else:

        print("No response...")


# Processes JSON data to extract list of centers with available slot and with needed age preferences
def availCenter(centerList):

    Lvalidcenters = []

    for center in centerList:
        for session in center['sessions']:
            if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                Lvalidcenters.append(center)

    
    return Lvalidcenters


main()

