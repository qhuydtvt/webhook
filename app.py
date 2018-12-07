from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
  print(request.get_json())
  return 200

if __name__ == '__main__':
  app.run(debug=True)