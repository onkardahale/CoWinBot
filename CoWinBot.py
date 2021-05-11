
import time
import json, requests
import pandas as pd

#supress pygame support message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

#API req url which is later appended with pincode and date as per user input
baseUrl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"

#Spoof User-Agent to bypass restrictions
headers_list = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}


# Main interface
def main():
    print("###########################################")
    print("#        CoWin Availablity Bot            #")
    print("###########################################")

    pincode = input("Enter pincode: ")
    date = input("Enter date: ")
    ageLimit = input("Enter minimum age limit:")
    
    count = 0
    #execute cowinApp(',') every 3 seconds
    starttime = time.time()
    while True:
        count = count + 1
        cowinApp(pincode, date, ageLimit, count)
        time.sleep(3 - ((time.time() - starttime) % 3))

#fn for constructing url from Pincode and Date input and pulling JSON data
def cowinApp(pincode, date, ageLimit, pingN):

    url = baseUrl + "pincode=" + pincode + "&date=" + date
    response = requests.get(url, headers=headers_list)

    #check for OK status
    if response.status_code == 200:

        jsonStr = json.loads(response.text)['centers']
        valid_centers = availCenter(jsonStr, ageLimit)

        df = pd.DataFrame(valid_centers, columns=['pincode', 'name', 'fee_type'])
        if len(df) > 0:
            print("###########################################")
            print("#          Available Centers              #")
            print("###########################################")
            print(df)

            alertSound()
            exit()
        else:
            print(f'No Available Centers: {pingN}')
    else:
        print("No response...")
        exit()

#Processes JSON data to extract list of centers with available slot and with needed age preferences
def availCenter(centerList , minAgeLimit):

    validcenters = []

    for center in centerList:
        for session in center['sessions']:
            if session['min_age_limit'] == minAgeLimit and session['available_capacity'] > 0:
                validcenters.append(center)

    return validcenters


# plays alert sound
def alertSound():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('notifSound.wav')
    my_sound.play(1)
    pygame.time.wait(int(my_sound.get_length()) * 2000)


main()

