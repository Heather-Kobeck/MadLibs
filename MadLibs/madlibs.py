###IMPORTS NEEDED LIBRARIES###
from os import remove
import yagmail
import csv
import random

###CREATES THE LISTS AND NEEDED VARIABLES###
nounList = []
adjList = []

sender = "email@email.com"
receiver = "email@email.com"
subject = "MadLibs!"







##FUNCTIONS AND DEFINITIONS##
def fillList(aList, aFile):
    """This reads from a csv file and adds each row 
        to a list using open(filename, read/writemode)
        //r for read w for write//
    Args:
        aList (list): [This is the list that will be filled]
        aFile (string): [name of the file being read from]
    """
    with open( aFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            aList.append(row[0])
    
    return aList       

  
def pickWord(aList):
    """This picks a random item from a list 
    then makes sure it cannot be picked again

    Args:
        aList (list): [This is the list the item will be picked from]
    """
    word = random.choice(aList)
    #print(word)
    aList.remove(word)
    #print(aList)
    return word


def sendEmail(aReceiver, aSender, aSubject, aBody):
    """This function will send an email with the info provided by the arguments

    Args:
        aReceiver (String): [The email address the message will be sent to ]
        aSender (String): [The email addrs that will be sending the email]
        aSubject (String): [The subject line of the email]
        aBody (String): [The message itself]
    """
    # define the sending email address
    yag = yagmail.SMTP(aSender)

    #send the email
    yag.send(
        to=aReceiver,
        subject=aSubject,
        contents=aBody,

    )





### CODE THAT RUNS ##

fillList(nounList, "nouns.csv")
fillList(adjList, "adjectives.csv")


messageFill = f"The {pickWord(adjList)} fairytale:\n Once upon a time there was a {pickWord(adjList)} {pickWord(nounList)} that wished to fly a {pickWord(nounList)}. It lived in a {pickWord(adjList)} castle in Romania. Also, in that castle lived a large {pickWord(nounList)} that was obsessed with a {pickWord(adjList)} {pickWord(nounList)}. Legend says its name is {pickWord(adjList)}{pickWord(nounList)}. The creatures in this castle were very {pickWord(adjList)} indeed.\n The End."


sendEmail(receiver,sender,subject,messageFill)

print("EMAIL SENT!!")


