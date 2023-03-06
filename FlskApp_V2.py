from flask import Flask, request, redirect, url_for
import csv, smtplib, ssl, random

app = Flask(__name__)

smtp_port = 587  # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "BankingSystemTest123@gmail.com"
pswd = "khfwiwmceczvkawg"


@app.route("/", methods = ["POST", "GET"])
def HomePage():
    # if request.method == "POST":
    #     Email = request.form["Email"]
    #     Pswd = request.form["Pswd"]
    #     if Email == "123" and Pswd == "123":
    #         return redirect(url_for("BallancePage", name = Email , bal = 1000))
    #     else:
    #         print("False")

    if request.method == "POST":
        Email = request.form["Email"]
        Pswd = request.form["Pswd"]
        with open('Details.csv', 'r', ) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if str(row[2]) == str(Email) and str(row[4]) == str(Pswd):
                    return redirect(url_for("BallancePage", name = Email , bal = 1000))
                else:
                    a = 1

                    ####
                    ### check to see if its the end of file if so return back to homepage 
                    ####
            file.close()
    else:
        return """<!DOCTYPE html>
            <html>
            
            <center><img src="umbrella.jpg" alt="Logo" width="450" height="128"></center>
            
            <body>
                <font size="4" face="OCR A Std Regular">
            
                    <form action="#" method="post">
                        <label for="Email"><center>Email:</center></label>
                        <center><input type="text" id="Email" name="Email"><br><br></center>
                        <label for="Pswd"><center>Password:</center></label>
                        <center><input type="text" id="Pswd" name="Pswd"></center><br><br></center>
                        <center><input type="submit" value="submit"/> <button type="button" >Create Account</button> <button    onclick="window.location.href='file:///U:/Desktop/stupid%20idea2.html';" type="button" >Forgot Password</button></center>
                    </form>
                
                 </font>
            
            </body>
            </html> """


@app.route("/<name>")
def BallancePage(name, bal):
    return f"""<!DOCTYPE html>
                <html>
                
                <center><img src="umbrella.jpg" alt="Logo" width="450" height="128"></center>
                
                <body><center>
                    <font size="4" face="OCR A Std Regular">
                
                    <p1>Account</p1>
                
                        <form action="/action_page.php">
                            <p1>ballance for {name} is {bal}</p1>
                            <button onclick="window.location.href='file:///U:/Desktop/account_Page.html';" type="button" >reload</button>
                        </form>
                    <font size="4" face="OCR A Std Regular">
                
                </center></body>"""

@app.route("Verification")
def Verification(email, code, methods = ["POST","GET"]):
    if request.method =="POST":
        UI_Code = request.form["code"]
        if UI_Code = code:
            return redirect(url_for("BallancePage", name = Email , bal = 1000))

        else:
            return redirect(url_for("HomePage"))

        
    else:
        returnf"""<!DOCTYPE html>
            <html>

            <center><img src="umbrella.jpg" alt="Logo" width="450" height="128"></center>

            <body><center>
                    <font size="4" face="OCR A Std Regular">

                    <p1>verification</p1>
                    <p1>please input the code sent to {email}</p1>

                            <form action="/action_page.php">
                              <label for="Email">Code:</label>
                              <input type="text" id="Code" name="Code"><br><br>
                              <button onclick="window.location.href='file:///U:/Desktop/stupid%20idea.html';" type="button" >back</button>
                            </form>
                    <font size="4" face="OCR A Std Regular">

            </center></body>"""



@app.route("/ForgotPassword", methods = ["POST","GET"])
def ForgotPassword():
    if request.method == "POST"
        Email = request.form["Email"]
        Ui = "resend"
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

        while Ui == "resend":
            code = ""
            for i in range(6): code = code + alphabet[int(random.randint(0, 25))]
            message = code.upper()
            simple_email_context = ssl.create_default_context()

            try:
                TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                TIE_server.starttls(context=simple_email_context)
                TIE_server.login(email_from, pswd)
                TIE_server.sendmail(email_from, Email, message)

            except Exception as e:print(e)
            finally:TIE_server.quit()
            return redirect(url_for("Verification", email = Email , code = code))
        
    else:
        return"""!DOCTYPE html>
                <html>

                <center><img src="umbrella.jpg" alt="Logo" width="450" height="128"></center>

                <body><center>
                        <font size="4" face="OCR A Std Regular">

                        <p1>Forgot Password</p1>

                                <form action="/action_page.php">
                                  <label for="Email">Email:</label>
                                  <input type="text" id="Email" name="Email"><br><br>
                                  <button onclick="window.location.href='file:///U:/Desktop/stupid%20idea.html';" type="button" >back</button>
                                </form>
                        <font size="4" face="OCR A Std Regular">

                </center></body>"""

if __name__ == "__main__":
    app.run()
