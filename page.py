from flask import Flask, render_template
from join import joins

app = Flask(__name__)
app.register_blueprint(joins, url_prefix ="/json")

@app.route("/")
def home():
    return render_template("index.html") 
if __name__ == '__main__':
    #< just edit here
    host = "127.0.0.1" #line 12: type your domain or server ip 
    port = 80          #line 13: type a port (http://your-domain.com:port) or (http://your-server-id:port)
    #just edit here />
    app.run(debug=True, port=port, host=host)
