# from flask import Flask, render_template, request, jsonify


# app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST']) # To render Homepage
# def home_page():
#     return render_template("index.html")



# if __name__ == '__main__':

#    # app.run(host="0.0.0.0", port=8080) #for deployment run
#     app.run(host="127.0.0.1", port=8080,debug=True) # for local run


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    if request.method == 'POST':
        return jsonify(message="Hello, this is a POST request")
    else:
        return "Hello, this is prince katiyar"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080) # for deployment run
    #app.run(host="127.0.0.1", port=8080, debug=True)
