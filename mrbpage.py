from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def mrb_home():
    return render_template('homepg.html')

@app.route('/contacts')
def mrb_contact():
    return render_template('contactas.html')
@app.route('/blog')
def mrb_blog():
    return render_template('blog.html')
@app.route('/websites')
def mrb_website():
    return render_template('websites.html')

if __name__ == "__main__" :
    app.run()