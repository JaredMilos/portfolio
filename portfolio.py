from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/mathapp')
def mathapp():
    return redirect('http://13.58.61.159/')

@app.route('/collabolab')
def collabolab():
    return redirect('http://18.222.110.209/')

if __name__=="__main__":
    app.run(debug=True) 
