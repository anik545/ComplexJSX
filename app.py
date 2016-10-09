from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/loci-plotter')
def loci():
    return render_template('loci.html')

@app.route('/operations-argand')
def operations():
    return render_template('operations.html')

if __name__=='__main__':
    app.debug = True
    app.run()
