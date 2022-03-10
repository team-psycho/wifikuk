# import module
import os
import requests

s = 1
# function to establish a new connection


def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>"""+name+"""</name>
	<SSIDConfig>
		<SSID>
			<name>"""+SSID+"""</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>"""+password+"""</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    s = os.system(command)

# function to connect to a network


def connect(name, SSID):
    command = "netsh wlan connect name=\""+name + \
        "\" ssid=\""+SSID+"\" interface=Wi-Fi"
    s = os.system(command)

# function to display avavilabe Wifi networks


def displayAvailableNetworks():
    command = "netsh wlan show networks interface=Wi-Fi"
    os.system(command)


# display available netwroks
displayAvailableNetworks()
try:
    pass_file = open("password.txt", "r")
    print("File Found")
except:
    print("No File Found")

api = "https://www.google.com/"
# try:
#     requests.get(api)
#     print("Found")
# except:
#     print("Not Found")

# input wifi name and password
name = input("Name of Wi-Fi: ")

for word in pass_file:
    # establish new connection
    createNewConnection(name, name, word)
    # connect to the wifi network
    connect(name, name)
    try:
        requests.get(api)
        print("Internet Connected")
        break
    except:
        print("Not Connected")

print("If you aren't connected to this network, try connecting with the correct password!")
