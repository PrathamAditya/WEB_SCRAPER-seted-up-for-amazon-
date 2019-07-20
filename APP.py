import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/dp/B07S58MHXF/ref=nav_ya_signin?th=1"

headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:9])

    if converted_price < 2.250:
        send_mail()

    print(converted_price)
    print(title.strip())

    if converted_price < 2.250:
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls
    server.ehlo()

    server.login("tha.noschourlias@yahoo.com", "kxjfrfzolygliuyb")

    subject = "price fell down!!"
    body = "Check the amamzon link: https://www.amazon.com/dp/B07S58MHXF/ref=nav_ya_signin?th=1"

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail("xourliman@yahoo.com", "tha.noschourlias@yahoo.com", msg)
    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()


while True:
    check_price()
    time.sleep(1.440)

