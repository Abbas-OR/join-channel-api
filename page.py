from flask import Flask, render_template
from join import joins

app = Flask(__name__)
app.register_blueprint(joins, url_prefix ="/json")

@app.route("/")
def home():
    return render_template("index.html") 
if __name__ == '__main__':
    app.run(debug=True, port=80, host="212.129.13.184")