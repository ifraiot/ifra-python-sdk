import ifra_sdk.client as ifra
import time


# Create new client
client = ifra.IfraSDK("<CHANNEL>","<DEVICE_ID>","<DEVICE_SECRET>")

counter=0
while True:
    
    #Append counter sensor
    client.addSensor("counter",'times', counter)

    #Send data
    client.send()

    #Sleep 1 sec
    time.sleep(1)  

    #Increase counter +1
    counter=counter+1