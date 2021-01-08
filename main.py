
from bs4 import BeautifulSoup

import requests
import smtplib

# driver = webdriver.Chrome()
URL = "https://www.flipkart.com/yonex-nanoflare-700-multicolor-strung-badminton-racquet/p/itmf1b14b6fddbb1?pid=RAQFX3FKHWV4PRAF&lid=LSTRAQFX3FKHWV4PRAFGVOTIF&marketplace=FLIPKART&srno=s_1_29&otracker=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&fm=SEARCH&iid=16668a2b-aee2-45c2-bf45-916b5242bfde.RAQFX3FKHWV4PRAF.SEARCH&ppt=sp&ppn=sp&ssid=fupfe836000000001609917581884&qH=019b0b27113bc3d1"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def send_mail():

    port = 456    # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "rrdtimepass@gmail.com"
    receiver_email = "raj.rishi441@gmail.com"
    password = "***********"
    sub = "racket price fell down"
    body =  """
    price fell down of the badminton
    check the link
    https://www.flipkart.com/yonex-nanoflare-700-multicolor-strung-badminton-racquet/p/itmf1b14b6fddbb1?pid=RAQFX3FKHWV4PRAF&lid=LSTRAQFX3FKHWV4PRAFGVOTIF&marketplace=FLIPKART&srno=s_1_29&otracker=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&fm=SEARCH&iid=16668a2b-aee2-45c2-bf45-916b5242bfde.RAQFX3FKHWV4PRAF.SEARCH&ppt=sp&ppn=sp&ssid=fupfe836000000001609917581884&qH=019b0b27113bc3d1
    
    """
    message =  "Subject:{}\n\n{}".format(sub,body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,"raj.rishi441@gmail.com",message)




def scrapper(URL):

    page = requests.get(URL)
    htmlcontent= page.content
    # print(htmlcontent)
    soup = BeautifulSoup(htmlcontent,"html.parser")

    # print(soup.get_text())
    name = soup.find("span",class_="B_NuCI")
    product_name = name.get_text()

    pricehtml = soup.find("div",class_="CEmiEU")
    price_block = pricehtml.get_text().replace("₹","-").split("-")
    price = float(price_block[1].replace(",",""))

    product=[product_name, price]

    print(product)

    if product[1]<10000:
        send_mail()
        print('_______________________________________')
    print("mail sent")
    return product



scrapper(URL)