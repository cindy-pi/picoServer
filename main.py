import hello
import wifi

## Import WiFi, expects your SSID and Password to be in secrets.py file
wifi.Connect()

## Starts you Web Service, it will display the index.html file.
webServer.Start()
