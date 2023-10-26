from flask import Flask

import json
from flask import render_template
from markupsafe import Markup
import sage_data_client


app = Flask(__name__, template_folder='templates')
@app.route('/')
def temperature():
    df = sage_data_client.query(
    start="-30m", 
    filter={
        "plugin": ".*plugin-iio.*",
        "vsn": "W071",
        "name": "env.temperature"
    }
    )
    #print(df)
    print(df)
    #print("type:", type(df))
    #print(df.groupby(["meta.vsn", "meta.sensor"]).value.agg(["size", "min", "max", "mean"]))
    title = "Past 30-minutes Temperature"
    temps0 = df[["timestamp","value"]]
    temps = temps0.copy()
    temps["timestamp"] = temps["timestamp"].astype(str)
    print(temps)
    d = temps.values.tolist()
    c = temps.columns.tolist()
    d.insert(0,c)
    tempdata = json.dumps({'title':title,'data':d})
    return render_template('temperatureVis.html', tempdata=tempdata)
