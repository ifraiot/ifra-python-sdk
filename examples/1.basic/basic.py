import ifra_sdk.client as ifra
import time


client = ifra.IfraSDK("2","2079ff2f-04e9-44d7-8bb9-7367ec235ae3","cfc8dc8d-1edf-4957-b62a-cb607a43409a")

i=0
while True:
    client.addSensor("cpu",'%',i)
    client.addSensor("ram",'GB',i)
    client.send()
    print("Test",i)
    time.sleep(1)
    i=i+1