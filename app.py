
from flask import Flask, render_template,request
import requests


app = Flask('weather')



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('spot')
        print(data)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={data}&appid=0c1f63f761e0caf78712ec7b00736ec0'
        api_data = requests.get(url)
        python_dict = api_data.json()
        print(python_dict)

        atmosphere = python_dict['weather'][0]['description']
        country = python_dict['sys']['country']
        wind = python_dict['wind']['speed']
        # location = python_dict['sys']['name']
        pressure = python_dict['main']['pressure']
        humidity = python_dict['main']['humidity']
        return render_template('weather.html', country = country , humidity = humidity ,pressure = pressure , data=data ,atmosphere= atmosphere, wind = wind)
    else:

        return render_template('weather.html')



app.run(port=8888)