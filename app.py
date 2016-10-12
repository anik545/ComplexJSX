from flask import Flask,render_template,request,jsonify
from complex_loci import *


app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/loci-plotter')
def loci():
    return render_template('loci.html')

@app.route('/_plot')
def plot():
    eq=request.args.get('eq',0,type=str)
    LHS,RHS=eq.split('=')
    lines=get_lines(LHS,RHS)
    lines=[str(x).replace('**','^') for x in lines]
    print(lines)
    return jsonify(result=lines) #TODO both curves in circle

@app.route('/operations-argand')
def operations():
    return render_template('operations.html')

if __name__=='__main__':
    app.debug = True
    app.run()
