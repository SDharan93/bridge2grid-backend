from flask import Flask, request, redirect
import twilio.twiml
import json

from Wiki import Wiki_feature

#Weather Imports
from forcast import Weather
import forecastio

#Finance Imports
from yahoo_finance import Share
from finance import Finance

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    #receving text
    rec_text = request.form['Body']
    resp = twilio.twiml.Response()

    #parsing text
    txt_msg = str(rec_text).split()

    if txt_msg[0] == "WIKI-FIND:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)
        #Returns possible results for query
        try:
            search_res = Wiki_feature.search(search_query)
        except:
            resp.message("There is no wiki pages related to your query.")
        else:
            resp.message("Possible Search results for '"+ search_query +"': \n" + ", \n".join(search_res))
    elif txt_msg[0] == "WIKI-SEARCH:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)
            #Returns possible results for query
        try:
            summary_res = Wiki_feature.summary(search_query)
        except:
            resp.message("Your query was not an exisiting wiki page, please use 'WIKI-FIND:' to retrieve the correct title and type it EXACTLY AS SHOWN")
        else:
            resp.message(summary_res)
    elif txt_msg[0] == "WEATHER:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        weatherObj = Weather(31.967819, 115.87718)
        resp.message(weatherObj.displayWeather(txt_msg[0]))
        resp.message(weatherObj.convertToJson())

    elif txt_msg[0] == "FINANCE:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        financeObj = Finance(txt_msg[0]) #companyCode
        resp.message(financeObj.displayFinance(txt_msg[1], txt_msg[2])) #yearStart, yearEnd
        resp.message(financeObj.convertToJson())
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
