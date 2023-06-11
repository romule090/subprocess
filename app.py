from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/run-command', methods=['POST'])
def run_command():
    command = request.form['command']
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return render_template('result.html', command=command, output=output)

if __name__ == '__main__':
    app.run()