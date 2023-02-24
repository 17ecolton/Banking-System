import smtplib
import ssl
import random

smtp_port = 587  # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "tedcolton177@gmail.com"
email_to = "edwincolton177@outlook.com"

pswd = "icmafrqbndfchnmd"


code = ""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

# content of message

for i in range(6) : code = code + alphabet[int(random.randint(0, 25))]
message = code.upper()

# Create context
simple_email_context = ssl.create_default_context()

try:
    # Connect to the server
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)

    # Send the actual email
    TIE_server.sendmail(email_from, email_to, message)

# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()
