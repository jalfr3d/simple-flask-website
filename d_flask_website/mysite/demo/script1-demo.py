from flask import Flask, render_template

app =Flask(__name__) #script executed __name__="__ main__" / imported __name__= "script1-demo" #name of file

@app.route('/') #route of link localhost:5000/(   )

def home():
    return render_template("home.html")

@app.route('/about/') 

def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
