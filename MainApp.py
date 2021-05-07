
import time
import json
import requests
import pandas as pd


#Get form url with PINCODE && DATE inputs from user
baseUrl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
#Spoof User-Agent to bypass restrictions
headers_dict = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}

# Main interface
def main():
    print("###########################################")
    print("#        CoWin Availablity Bot            #")
    print("###########################################")

    pincode = input("Enter pincode: ")
    date = input("Enter date: ")

    #execute cowinApp(',') every 3 seconds
    starttime = time.time()
    while True:
        cowinApp(pincode, date)
        time.sleep(3 - ((time.time() - starttime) % 3))

#fn for Pincode and Date input and pulling JSON data
def cowinApp(pincode,date):

    url = baseUrl + "pincode=" + pincode + "&date=" + date
    response = requests.get(url, headers=headers_dict)

    #check for OK status
    if response.status_code == 200:
        jsonStr = json.loads(response.text)['centers']
        valid_centers = availCenter(jsonStr)

        df = pd.DataFrame(valid_centers, columns=['name', 'address', 'fee_type'])
        if len(df):
            print("###########################################")
            print("###########Available Centers###############")
            print("###########################################")
            print(df)
            #        plotTable(df)
        else:
            print("No Available Centers")
    else:
        print("No response...")

#Processes JSON data to extract list of centers with available slot and with needed age preferences
def availCenter(centerList):
    validcenters = []
    for center in centerList:
        for session in center['sessions']:
            if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                validcenters.append(center)
    return validcenters

''''
#plot pandas DataFrame to get image sendable by email (hope for future)
def plotTable(dataframe):
    ax = pyplot.subplot(111, frame_on=True)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    table(ax, dataframe)

    pyplot.savefig('table.png')
''''

main()
