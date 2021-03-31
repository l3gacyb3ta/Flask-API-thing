from flask import Flask, render_template, request
import requests

web_site = Flask(__name__)


@web_site.route('/')
def index():
  r = requests.get("http://0.0.0.0:5000/names")
  dat = r.json()
  return render_template('index.html',data=dat, leng=len(dat))

@web_site.route('/addname')
def add():
  return render_template('add_name.html')

@web_site.route('/handledata', methods=['POST'])
def handledata():
  gottenname = request.form['name']
  requests.post("http://0.0.0.0:5000/names", {gottenname:''})
  return render_template('name_added.html', name=gottenname)

web_site.run(host='localhost', port=8080)