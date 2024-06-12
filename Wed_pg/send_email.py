import smtplib, ssl

def send_email(message):
    host = "smtp.gamil.com"
    port = 465

    username = ""
    password = ""

    receiver = ""
    context = ssl.create_default_context()

    message = """\
    Subject: hi
    How are you?
    Bye..."""

    with smtplib.SMPT_SSL(host, port, conetxt=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)