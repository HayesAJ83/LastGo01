import os.path
from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_url_path='/assets')

@app.route('/')
def index():
    return render_template('/pages/index.html')

if __name__ == "__main__":
    app.run(Debug=True)
