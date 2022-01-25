from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def first_checkerboard():
    return render_template("index.html")

@app.route('/4')
def second_checkerboard():
  return render_template("four.html")

@app.route('/<int:x>/<int:y>')
def third_checkerboard(x, y):

  return render_template("variableboard.html", x=x, y=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def fourth_checkerboard(x, y, color1, color2):

  return render_template("fourvariables.html", x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)