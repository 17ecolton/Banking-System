from flask import Flask, request, redirect, url_for
import csv, smtplib, ssl, random

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run()
