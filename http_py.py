import bottle

app = bottle.Bottle()

@app.route('/fuck-you')
def shit():
    return "fuck you."

@app.route('/')
@app.route('/fuck-you/<name>')
def personal(name = 'motherfucker'):
    return bottle.template('Hey {{name}}, fuck you.', name = name)

@app.route('/bleep/<times:int>')
def repetition(times):
    text = ""
    for i in range(times):
        text += "fuck you "
    return text

@app.route('/bleep/<name:path>')
def bleep(name = 'bleep'):
    return bottle.template('Hey {{name}}, bleep you.', name = name)



@bottle.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

login_dict = {'dolha':'guinho'}

def check_login(user, pwd):
    if user in login_dict and login_dict[user] == pwd:
        return True
    else:
        return False

@bottle.post('/login') # or @route('/login', method='POST')
def do_login():
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"



# bottle.run(host='localhost', port=8080, debug=True)
bottle.run(app, host='localhost', port=8080)