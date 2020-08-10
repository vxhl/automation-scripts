# Import the requests and bs4 with pip install requests bs4
import requests
from bs4 import BeautifulSoup
import smtplib
import time
# Add the URL for the product you want to track. I am adding one from Amazon for a laptop I'm looking to buy.
URL = 'https://www.amazon.in/Acer-15-6-inch-Graphics-Obsidian-AN515-54/dp/B088FLW4TW/ref=sr_1_1?crid=2H41SHLUNLX4C&dchild=1&keywords=acer+tuf+gaming+laptop&qid=1596998484&sprefix=Acer+tuf+%2Caps%2C368&sr=8-1'

# Search on google to get you User-Agent by typing "My User Agent" and paste it in a string under the key User-Agent
headers = {"User-Agent" :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

# The function for checking the price
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text() # Gets the name of the product using the HTML element id. You can look for this by inspecting over the name in the browser and copying the id from the HTML tag
    price = soup.find(id="priceblock_ourprice").get_text() # Same for Price
    price2 = price.replace(',','.') # Replace the  commas with dots as the price is a string and we need to convert it into float for comaparison
    converted_price = float(price2[2:8]) # We slice the integer values as the special symbols cannot be converted as a string
    #print(converted_price)

    if(converted_price <= 55.0): # Here 55.0 stands for 55K and it depicts the values below which the email will be send
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    # For logging in you use your gmail id and as for the password
    # Generating Password : If you do not already have a two factor authentication set for your gmail account do that first by going to Google 2 Step Verification
    # After that is done type "Google App Passwords" and set up the app for mail and for whatever system you are using. That will generate the 14 letter password  
    server.login('moharibishal@gmail.com','mfielbfkosdkvzph')
    
    # Here we set the subject and body for our mail 
    subject = ' Price fell down !'
    body = 'Check the amazon link https://www.amazon.in/Acer-15-6-inch-Graphics-Obsidian-AN515-54/dp/B088FLW4TW/ref=sr_1_1?crid=2H41SHLUNLX4C&dchild=1&keywords=acer+tuf+gaming+laptop&qid=1596998484&sprefix=Acer+tuf+%2Caps%2C368&sr=8-1 and ring your father up right now! This is fucking amazing.'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'moharibishal@gmail.com',
        'xyz@gmail.com',
         msg
    )
    print('EMAIL SENT !')

    server.quit()
# Now we generate an infinite while loop that will keep checking our price and send the mail if the price goes down
while(True):
    check_price()
    time.sleep(60*60)


