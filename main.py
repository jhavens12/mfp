import myfitnesspal
import pprint
import credentials
import json
import requests
import datetime



def post_sensor(sensor,data):
    headers = {"Authorization": "Bearer "+credentials.api_token,
               'content-type': 'application/json'}

    url = credentials.api_url+"/api/states/"+sensor
    #data = '{"state": "1", "attributes": {"unit_of_measurement": "Miles"}}'
    response = requests.post(url, headers=headers, data=data)
    print("Posting Sensor: ",sensor)
    #print(response.text)

client = myfitnesspal.Client(credentials.mfp_username, password=credentials.mfp_password)
timestamp = datetime.datetime.now()

day = client.get_date(timestamp.year, timestamp.month, timestamp.day)
total = int(day.totals['calories'])
goal = int(day.goals['calories'])
remaining = goal - total
print(remaining)

sensor = {}
sensor['state'] = remaining
sensor['attributes'] = {}
sensor['attributes']['calories_consumed'] = total
sensor['attributes']['calorie_goal'] = goal
sensor['attributes']['carbohydrates'] = day.totals['carbohydrates']
sensor['attributes']['fat'] = day.totals['fat']
sensor['attributes']['protein'] = day.totals['protein']
sensor['attributes']['sodium'] = day.totals['sodium']
sensor['attributes']['sugar'] = day.totals['sugar']

sensor_name = "sensor.mfp_remaining"
post_sensor(sensor_name,json.dumps(sensor))
