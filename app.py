from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Maria Jimenez! I am adding my first code change.'


@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():  # put application's code here
    return render_template('about-css.html')

@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():  # put application's code here
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        birthday = request.form['birthday']
        return render_template('contact.html', submitted=True, first_name=first_name, last_name=last_name, email=email, birthday=birthday)
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run()
