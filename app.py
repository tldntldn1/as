from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hi():
    return render_template('hi.html')


if __name__ == '__main__':
    app.run()
