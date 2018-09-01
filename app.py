from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


# Automatically reload the application upon a template file change
app.config['TEMPLATES_AUTO_RELOAD'] = True

#run the application
port = 5000
app.run(host="0.0.0.0", port=port, debug=True)
