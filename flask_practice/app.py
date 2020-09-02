from flask import Flask , url_for,redirect,render_template,request,session , flash


app = Flask(__name__)
app.secret_key='secret'

@app.route('/')
def home ():
    return render_template('base.html',title = 'HOME')

@app.route('/profile')
def profile():
    return render_template('base.html',title = 'PROFILE')

@app.route('/index')
def index():
    return render_template('index.html',title = 'INDEX')
    
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        session.permanent=False
        name=request.form['nm']
        session['user']=name
        flash(f'{name} logged in successfully !')
        return redirect(url_for("username",nm=name))
    else:
        if "user" in session:
            name=session['user']
            flash(f'{name} already logged in !')
            return redirect(url_for('username')) 

        return render_template('login.html')
    

@app.route('/user')
# value in <> allows to pass parameters to the function from other pages
def username():
    if "user" in session :
        user=session['user']
        
        return render_template('user.html',user=user)
    else:
        return redirect(url_for('login'))

# @app.route('/admin/')
# def admin():
#     return redirect(url_for('name',name='Admin!'))

@app.route('/logout')
def logout():

    if 'user' in session:
        user=session['user']
        session.pop('user',None)
        flash(f'You\'ve been logged out {user}')
    
    return redirect(url_for('login'))

   


if __name__ == "__main__":
    
    app.run(debug=True)


