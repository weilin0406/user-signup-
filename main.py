from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
no_spec_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

@app.route('/', methods=['GET', 'POST'])

def signup_form(): 

        if request.method == 'GET': 
                return render_template('Sign_up.html') 


        if request.method == 'POST':
                username_error = ''
                password_error = ''
                password_verify_error = ''
                email_error = ''

                username = request.form['username_name']
                password = request.form['password_name']
                password_verify = request.form['password_verify']
                email = request.form['email_name']  

                email_at_counter = 0
                email_dot_counter = 0

                if username:

                        for i in username: 
                                if i not in no_spec_char:
                                        username_error = "Not Valid: Use only Alphabet and Numbers."

                                if len(username) < 3 or len(username) > 20:
                                        username_error = 'Username needs to be 3-20 characters.'
                                     
                else:
                        username_error = "Username field is Blank."

                if not len(password): 
                        password_error = "Password field is Blank."  

                if len(password) < 3 or len(password) > 20: 
                                        password_error = 'Password must be 3-20 characters and not contain spaces.' 
                if " " in password:
                        password_error = "Not Valid: Do not use space in Password."
                if " " in password_verify:
                        password_verify_error = "Not Valid: Do not use space in Password."

                        
                      
                
                if password_verify != password: 
                        password_verify_error = 'Passwords do not match.' 
        
                if email:
                        for i in email:
                                if i =='@':
                                        email_at_counter += 1
                                if i =='.':
                                        email_dot_counter += 1
                        if email_dot_counter == 0 and email_at_counter == 0:

                                email_error = "Enter a Valid  E-mail."
                        if len(email) < 3 or len(email) > 20:
                                email_error = 'Not Valid: E-mail length must be longer than 3 or shorter than 20 characters long.'
                        if email_at_counter > 1 or email_dot_counter > 1 or " " in email:
                                email_error = 'Ener a Valid E-mail.'

  
 
                if not username_error and not password_error and not password_verify_error and not email_error: 
                        return redirect('/welcome?username={0}'.format(username)) 
  
 
                return render_template('sign_up.html', username_value=username, email_value=email, 
                             username_error=username_error, password_error=password_error, 
                             password_verify_error=password_verify_error, email_error=email_error) 

@app.route('/welcome')
def welcome():

        username = request.args.get('username') 
        return render_template('welcome.html',title="Welcome!", username=username) 
 
app.run()