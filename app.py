from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/download')
def download_resume():
    resume_path = 'static/resume.pdf'
    return send_file(resume_path, as_attachment=True, attachment_filename='resume.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
  