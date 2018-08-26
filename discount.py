from flask import Flask, render_template, redirect, \
      url_for, request, session, flash, g

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def total_amount(self):
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)