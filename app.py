from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pandas as pd

app = Flask(__name__)

News = [
  {
    'id': 1,
    'link': 'economictimes.com',
    'headline': '360 One raises funds',
    'description': 'The management raised 4B$',
    'date': 'Aug 18 2023'
  },
  {
    'id': 2,
    'link': 'livemint.com',
    'headline': 'IIFL One raises funds',
    'description': 'The management raised 4B$',
    'date': 'Aug 17 2023'
  },
]

articles = pd.read_excel('TestData123.xlsx')
json_obj = articles.to_dict(orient='records')
print(json_obj)

statusUpdate = []
relevantList = []
newNews = []
df = pd.DataFrame()
counter = int(json_obj[-1]['id'])


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=json_obj)


@app.route("/saveData", methods=['POST'])
def savedData():
  if request.method == 'POST':
    values = request.form.getlist('check1')
    for i in range(len(values)):
      json_obj[i]['status'] = values[i]
      print(json_obj)
  return render_template('clickAddNew.html', jobs=json_obj)


@app.route("/addNew", methods=['GET', 'POST'])
def addNew():
  global counter
  print(counter)
  newNewsDict = {}
  todayDate = datetime.now().strftime('%b %d %Y')
  if request.method == 'POST':

    link = request.form.get('link')
    headline = request.form.get('headline')
    description = request.form.get('description')
    if link is not None:
      counter += 1
      newNewsDict['link'] = link
      newNewsDict['headline'] = headline
      newNewsDict['article_text'] = description
      newNewsDict['Date'] = todayDate
      newNewsDict['id'] = counter
      newNewsDict['status'] = 'Relevant'
      json_obj.append(newNewsDict)
  return render_template('addNew.html', jobs=json_obj)


@app.route("/finalData", methods=['POST'])
def final():
  if request.method == 'POST':
    return render_template('final.html', jobs=json_obj)


@app.route("/submitPage", methods=['POST'])
def submit():
  if request.method == 'POST':
    df = pd.DataFrame(json_obj)
    df = df[df['status'] == 'Relevant']
    print(df)
    todayDate = datetime.now().strftime('%b%d%Y')
    fileName = 'Relevant' + str(todayDate) + '.xlsx'
    df.to_excel(fileName)
  return "Submitted Successfully"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
