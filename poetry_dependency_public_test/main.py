import flask
import httplib2

app = flask.Flask(__name__)
http = httplib2.Http()

IP_FETCHER_URL = "http://ipinfo.io/ip"

@app.route("/")
def hello_world():
    response, content = http.request(IP_FETCHER_URL)
    if response["status"] != "200":
        return ("Failed to get IP address ({}): {}".format(response["status"], content.decode("utf-8")), 503)

    return "Server outbound IP address appears to be: {}".format(content.decode("utf-8"))
