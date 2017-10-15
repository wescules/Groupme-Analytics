import requests
import time

# Some variables that will be used in making calls to the APIs
location_name = 'Houston, TX'
location_coords = { 'x': '29.7199', 'y': '-95.3422' }
request_params = { 'token': 'kAZbsItBcTqgSi0GbKkTBnruHxH4AfjRijrlJsOV'}

while True:

    response = requests.get('https://api.groupme.com/v3/groups/35291456/messages', params = request_params)

    # If there are new messages, check whether any of them are making queries to the bot
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']

        # Iterate through each message, checking its text
        for message in response_messages:
            mess = message['text'].lower()
            if mess.find('weather') > -1:
                weather_response = requests.get('https://api.weather.gov/points/' + location_coords['x'] + ',' + location_coords['y'] + '/forecast').json()
                current_weather = weather_response['properties']['periods'][0]['detailedForecast']
                to_send = 'Weather for ' + location_name + ': ' + current_weather
                print('Weather for ' + location_name + ': ' + current_weather)
                post_params = { 'bot_id' : 'ab6285d54cd427c80db274e2e1', 'text': to_send }
                requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
                request_params['since_id'] = message['id']
                break
            if mess.find('he') > -1:
                print('HE??!')
                break
            if mess.find('she') > -1:
                print('SHE??!')
                break
            if mess.find('nigger') > -1 or mess.find('nigga') > -1:
                 print('Woah there! Next time, please refrain from using this horribly racist word. Instead, please use the universally accepted term "Basketball American".\nThanks for understanding')
                 break



            # if(message['text'].lower() == "he"):
            #
            #     to_send = 'HE???!'
            #     # Send the response to the group
            #     post_params = { 'bot_id' : 'ab6285d54cd427c80db274e2e1', 'text': to_send }
            #     requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
            #     request_params['since_id'] = message['id']
            #     print("sending message: " + to_send)
            #     break
            #
            #
            # if(message['text'].lower() == "she"):
            #
            #     to_send = 'SHE???!'
            #     # Send the response to the group
            #     post_params = { 'bot_id' : 'ab6285d54cd427c80db274e2e1', 'text': to_send }
            #     requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
            #     request_params['since_id'] = message['id']
            #     print("sending message: " + to_send)
            #     break
            #
            #
            # if(message['text'].lower() == "nigger" or message['text'].lower() == "nigga"):
            #
            #     to_send = 'Woah there! Next time, please refrain from using this horribly racist word. Instead, please use the universally accepted term "Basketball American".\nThanks for understanding'
            #     # Send the response to the group
            #     post_params = { 'bot_id' : 'ab6285d54cd427c80db274e2e1', 'text': to_send }
            #     requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
            #     request_params['since_id'] = message['id']
            #     print("sending message: " + to_send)
            #     break
            #
            #
            # if (message['text'].lower() == 'weather'):
            #
            #     # Construct a response to send to the group
            #     weather_response = requests.get('https://api.weather.gov/points/' + location_coords['x'] + ',' + location_coords['y'] + '/forecast').json()
            #     current_weather = weather_response['properties']['periods'][0]['detailedForecast']
            #     to_send = 'Weather for ' + location_name + ': ' + current_weather
            #
            #     # Send the response to the group
            #     post_params = { 'bot_id' : 'ab6285d54cd427c80db274e2e1', 'text': to_send }
            #     requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
            #     request_params['since_id'] = message['id']
            #     print("sending message: " + to_send)
            #     break

    time.sleep(3)
