# CoWinApp

CoWinApp checks availablity of vaccination slots for given Pincode and date.  
It pulls a list of centers with minimum age limit as 18 and greater than 0 available slot in JSON format and outputs the list in a tabular format.

The CoWin API has blocked scripts but CoWinApp handles that by spoofing User-Agent header.

----

## Prerequisite libraries

- **[requests](https://pypi.org/project/requests/)**
- **[pandas](https://pypi.org/project/pandas/)**

#### Installation commands
    pip install requests
    pip install pandas

----

## Usage Details
CoWinApp pings the API every 3 seconds.
For this, it needs you to keep the **computer on** for the **entire time**.

1. Turn off auto-sleep  
2. The API is geo-fenced and throws 403 Error for all requests not from India.
3. Enter the date in DD-MM-YYYY format
