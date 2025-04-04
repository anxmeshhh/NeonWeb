from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# MySQL Configuration
db = pymysql.connect(
    host="localhost",        # Or Neon host
    user="root",
    password="theanimesh2005",
    database="neonweb"
)

@app.route('/')
def index():
    return render_template('index.html')  # Make sure your HTML file is named form.html

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    website_type = request.form.get('website-type')
    budget = request.form.get('budget')
    features = request.form.get('features')
    deadline = request.form.get('deadline')
    github_integration = 'Yes' if request.form.get('github-integration') else 'No'
    
    cursor = db.cursor()
    sql = """
        INSERT INTO orders (name, email, website_type, budget, features, deadline, github_integration)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (name, email, website_type, budget, features, deadline, github_integration))
    db.commit()
    cursor.close()
    
    return redirect('/')
@app.route('/contact', methods=['POST'])
def contact():
    name_id = request.form.get('contact-name')  # This is the value entered by user
    email_id = request.form.get('contact-email')
    message_id = request.form.get('contact-message')

    cursor = db.cursor()
    cursor.execute("INSERT INTO contact_ids (name_id, email_id, message_id) VALUES (%s, %s, %s)", 
                   (name_id, email_id, message_id))
    db.commit()
    cursor.close()

    return redirect('/')  # or return a success message


if __name__ == '__main__':
    app.run(debug=True)
