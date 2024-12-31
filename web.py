from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Xin chào!</h1>"

@app.route("/gioi-thieu")
def gioi_thieu():
  return "<h2>Đây là trang giới thiệu</h2>"

if __name__ == "__main__":
  app.run(debug=Tru