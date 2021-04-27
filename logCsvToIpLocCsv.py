#Import required libs
import requests
import csv

#Open the CSV log file into the object 'file' with read perms
file = open('exampleData.csv', 'r')

#Thease are the required varables to read the file
arrayofcsv = [] # the aray we're saveing the file in
count = 0 # a counter

#Reads the file line by line
while True:
    count += 1

    # Get next line from file
    line = file.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    line = line.strip() #removes newline characters
    arrayofcsv.append(line.split(","))  # Each new word seporated by a ',' is a
                                        # new array item
                                        # Eg: "Hello,World" -> ["Hello", "World"]

# This line removes the coloum headers from the csv file data imported
# We dont need the headers as we know the order the data will be in
arrayofcsv.remove(arrayofcsv[0])

#The rowlist that is writen to the CSV file
#The first row is the table headers and is pre-populated here
csvFileOut = [["Ip Addrs","Country"]]

# For every item in the array of the CSV file we reach out to an api hosted in
# the cloud to get the contry name for that IP address
for entry in arrayofcsv:

    #The get request is made by joining the api's web address with the ip and api variables we need
    getRequest = "https://geolocation-db.com/json/" + entry[1] + "&position=true"

    # The responsse is then saved to a var as a json datatype
    # The json is reterned from a http request made with the requests python module
    response = requests.get(getRequest).json()

    #This line parses the json for the contry name and appends it to the output array with the ip address
    csvFileOut.append([str(entry[1]),str(response["country_name"])])


# Opens the csv file we're writing with write perms
with open('exampleIpCountry.csv', 'w', newline='') as csvFile:
    # Creates the object used to write to a csv file
    writer = csv.writer(csvFile)
    # Writes the 2D array to the csv file
    writer.writerows(csvFileOut)
