import json
from flask import render_template
import sage_data_client
import pandas as pd

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
#df[["timestamp"]] = df['timestamp'].dt.strftime('%H:%M:%S')
print(df)
temps = df[["timestamp","value"]]
temps["timestamp"] = temps["timestamp"].astype(str)
d = temps.values.tolist()
c = temps.columns.tolist()
d.insert(0,c)
tempdata = json.dumps({'title':title,'data':d})

# {
#     cols: [{id: 'task', label: 'Task', type: 'string'},
#            {id: 'hours', label: 'Hours per Day', type: 'number'}],
#     rows: [{c:[{v: 'Work'}, {v: 11}]},
#            {c:[{v: 'Eat'}, {v: 2}]},
#            {c:[{v: 'Commute'}, {v: 2}]},
#            {c:[{v: 'Watch TV'}, {v:2}]},
#            {c:[{v: 'Sleep'}, {v:7, f:'7.000'}]}]
#     }

formatedData = '{cols: [{id: "timestamp", label: "Timestamp" type: "string"}, {id: "value", label: "Temperature", type: "number"}], rows: []}'
#for i in
print(type(formatedData)) 
print(temps)
print("curr", type(temps))

