from flask import Flask, request, render_template, redirect,flash, session

app = Flask(__name__)
app.secret_key = "asdfd"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    print "Got the info."
    if len(request.form["name"]) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    else:
        flash("Success! Your name is {}".format(request.form['name']))
        name = request.form["name"]   
    location = request.form['location']
    language = request.form['language']

    if len(request.form["comment"]) < 1:
        flash("Comment cannot be empty!")
        return redirect('/')
    elif len(request.form["comment"]) > 120:
        flash("Comment cannot be more than 120 characters!")
        return redirect('/')
    else:
        flash("Success!")
        comment = request.form['comment']
    return render_template('result.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True)