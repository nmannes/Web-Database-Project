import flask
from flask import render_template
import sys
import datasource
import numpy as np

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/results/<var>')
def get_results_1_variable(var):
    ds = datasource.DataSource()
    validVars = np.load('varList.npy')
    if var not in validVars:
        return render_template('error.html')
    else:
        ds.runQuery([var, ""])
        ds.createGraph()
        queryStats = ds.getStats()
        return render_template('results.html', 
                                stats=queryStats, 
                                var1 = var, var2 = "")
                                
@app.route('/results/<var1>/<var2>')
def get_results_2_variables(var1, var2):
    ds = datasource.DataSource()
    validVars = np.load('varList.npy')
    if var1 not in validVars or var2 not in validVars:
        return render_template('error.html')
    else:
        ds.runQuery([var1, var2])
        ds.createGraph()
        queryStats = ds.getStats()
        return render_template('results.html', 
                                stats=queryStats, 
                                var1 = var1, var2 = var2)
                                
@app.route('/second/<var>')
def get_second(var):
    print(var)
    return render_template('second.html', var = var)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
