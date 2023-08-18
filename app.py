from flask import Flask,render_template

app = Flask(__name__)

News=[
  {
    'link':'economictimes.com',
    'headline':'360 One raises funds',
    'description':'The management raised 4B$',
    'date': 'Aug 18 2023'
  },
   {
    'link':'livemint.com',
    'headline':'IIFL One raises funds',
    'description':'The management raised 4B$',
    'date': 'Aug 17 2023'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=News)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
