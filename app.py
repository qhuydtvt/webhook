from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    return request.args.get('hub.challenge')
  else:
    print(request.get_json())
    return "OK"

if __name__ == '__main__':
  app.run(debug=True)