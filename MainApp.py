
import json, requests

def main():

	print("CoWin Availablity Bot")
	print("------------------------------------------")

	#Get form url with PINCODE && DATE inputs from user
	baseUrl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=400607&date=07-05-2021"

#	pincode = input("Enter pincode: ")
#	date = input("Enter date: ")

	headers_dict = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
#	url = baseUrl + "pincode=" + pincode + "&date=" + date
#	print(url)

	response = requests.get(baseUrl, headers=headers_dict)
	print(response.text)



main()
