# Random Password Generator Flask App


from flask import Flask, request, render_template
from datetime import datetime
import random
import string


#### Defining the Flask App

app = Flask(__name__)

### Saving Date today in 2 different formats

date_today = datetime.today().strftime("%m_%d_%y")
date_today2 = datetime.today().strftime("%d-%B-%d")

############ Routing Function ###########

#### our main page

@app.route('/')
def home():
    return render_template('home.html', date_today2 = date_today2)


@app.route('/gen_password',methods=['GET','POST'])
def gen_password():
    min_pass_len = 6 
    max_pass_len = 50


    pass_len = int(request.form.get('pass_len'))


    if pass_len<min_pass_len:
        return render_template('home.html', date_today2 = date_today2, mess=f'Atleast create a {min_pass_len} digit password...')

    if pass_len>max_pass_len:
        return render_template('home.html', date_today2 = date_today2, mess=f'Can create a max {max_pass_len} digit password...') 
    
    include_spaces = request.form.get('include_spaces')
    include_numbers = request.form.get('include_numbers')
    include_special_chars = request.form.get('include_special_chars')
    include_uppercase_letters = request.form.get('include_uppercase_letters')


    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    print(include_spaces, include_numbers, include_special_chars, include_uppercase_letters)

    char_sets = [lowercase_letters]


    # Add character sets based on the parameters

    if include_spaces == 'on':
        char_sets.append(' ')
    if include_numbers == 'on':
        char_sets.append(' ')
    if include_special_chars == 'on':
        char_sets.append(' ')
    if include_uppercase_letters == 'on':
        char_sets.append(' ')

    # Combine the character sets
    all_chars = ''.join(char_sets)

    password = random.choices(all_chars, k=pass_len)
    password = ''.join(password)


    return render_template('home.html', date_today2 = date_today2, generated_password = password)


#### Our main function which runs the random password generator Flask app
if __name__ == '__main__':
    app.run(debug=True)