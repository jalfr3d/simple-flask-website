from flask import Flask, render_template

# script execute __name__="__ main__" / imported __name__= "script1-demo" the name of file
app =Flask(__name__)

# route is localhost:5000/(   )


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/') 
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
