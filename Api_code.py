import requests

API_key = '58ce9baf526e8b8660d0983e9f60f84a'
city_name = input('Enter the City name: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric' #unit Metric used to change the temp kelvin to Cel

response = requests.get(url)  

if response.status_code == 200:
    
    print('Yupee... you want to know the weather.')
    data = response.json()
    #print(data) # Check if we are getting result from API call
    print('Weather is:', data['weather'][0]['description'])  #0 to access the list 
    print('Current temp is:', data['main']['temp']) 
else:
    print('Not able to find the City/Data. Status code:', response.status_code)
