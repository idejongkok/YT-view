from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import time
import random2
from selenium import webdriver
#start Proxy
initialize_VPN(save=1)

#initialize webdriver to automate the browser
driver = webdriver.Chrome()

#random URL
Rest_URL = ['https://google.com/','https://idejongkok.xyz/','https://youtube.com']
sleep_time = 0

#User's inputs
LinkURL = input("Enter Youtube Link: ",)
Views = int(input("Enter Views: ",))
MinDuration = int(input("Enter Minimum Duration to watch: ",))
MaxDuration = int(input("Enter Maximum Duration to watch: ",))
driver.minimize_window()

#Loops

for i in range(Views):
    #switch ip address with NordVPN
    rotate_VPN()

    #Get notice for view attemps
    print ("Watching for {} time" .format(i+1))
    
    # open URL
    driver.get(LinkURL)

    # Set approx watch time / duration
    sleep_time = random2.randint(MinDuration, MaxDuration)
    print("Will playing for: ",sleep_time, " secs")
    time.sleep(sleep_time)

    # Open a random URL to try to manipulate youtube logic 
    random_URL = random2.randint(0,2)
    driver.get(Rest_URL[random_URL])
    time.sleep(3)

driver.quit()
terminate_VPN()

