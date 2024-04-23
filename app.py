from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the socials page
@app.route('/socials')
def socials():
    return render_template('socials.html')

# Route for the experience page
@app.route('/experience')
def experience():
    return render_template('experience.html')

if __name__ == '__main__':
    app.run(debug=True)