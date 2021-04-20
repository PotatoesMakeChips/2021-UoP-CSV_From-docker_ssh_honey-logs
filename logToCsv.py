#Import required libs
import csv

#Open the log file into the object 'file' with read perms
file = open('example.txt', 'r')

#Key Defs

count = 0 #counter used for reading the log file line by line

#a dict to convert from the three letter mounth abrevations to a number that excel can process
mounthToNumber = dict(
Jan=1,
Feb=2,
Mar=3,
Apr=4,
May=5,
Jun=6,
Jul=7,
Aug=8,
Sep=9,
Oct=10,
Nov=11,
Dec=12
)

#The rowlist that is writen to the CSV file
#The first row is the table headers and is pre-populated here
rowList = [["Time","Ip Addrs","Username","Password"]]

#Reads the file line by line
while True:
    count += 1

    # Get next line from file
    fileLine = file.readline()

    # if line is empty
    # end of file is reached
    if not fileLine:
        break
    dataLine = fileLine.strip() #removes newline characters

    #splits line into an array list
    dataAray = dataLine.split() #Each new word is a new array item
                                #Eg: "Hello World" -> ["Hello", "World"]

    #Gets the year from the dataAray line
    year = dataAray[4]
    #There is a trailing ] on the year so it it removed with string sliceing
    year = year[:-1] # [:-1] removes the lasrt character from the string

    #Gets the mounth from the dataAray line
    #The dictionary is used to convert the mounth to a number
    mounth = mounthToNumber[str(dataAray[1])] # The datatype is forced to ensure the dict works.
                                              # This isn't technicaly needed but will hopefuly
                                              # prevent issues in the future

    #Concatinates the date and time as a string
    #This string follows the ISO guidance for storing dates
    date = str(year) + "-" + str(mounth) + "-" + str(dataAray[2]) + " " + str(dataAray[3])

    #Gets the other datapoints as strings. Datatype is forced for same reason as above
    ipAddress = str(dataAray[5])
    username = str(dataAray[6])
    password = str(dataAray[7])

    #Creates an array list of the data we want to write to the csv file
    csvLine = [date,ipAddress,username,password]

    #Appends the csvLine array to the array that is writen to the file
    rowList.append(csvLine)

# Closes the log file to prevent damage to data
file.close()

# Opens the csv file with write perms
with open('protagonist.csv', 'w', newline='') as csvFile:
    # Creates the object used to write to a csv file
    writer = csv.writer(csvFile)
    # Writes the 2D array to the csv file
    writer.writerows(rowList)
