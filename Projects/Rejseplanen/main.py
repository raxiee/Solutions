import json
import requests

read_from_file = False
def json_stub():
    x = 2
    if read_from_file:
        with open("insert_filename_here.json", 'r') as f:
            dic = json.loads(f.read())  # invoke json.loads() on the contents of the file, as opposed to the file path of that JSON
        print(dic)
    else:  # read from web
        r = requests.get('https://xmlopen.rejseplanen.dk/bin/rest.exe/trip?originId=8600626&destCoordX=12276500&destCoordY=55648300&destCoordName=H%C3%B8jeTaastrup&date=19.09.24&time=19:02&useBus=0&format=json')
        print(r.json()['TripList']["Trip"]["x"])
        # print(r.json()TripList.Trip[1].Leg[0].Origin.date)

json_stub()