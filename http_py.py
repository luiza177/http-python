import bottle

app = bottle.Bottle()

@app.route('/shit')
def shit():
    return "fuck you."

# bottle.run(host='localhost', port=8080, debug=True)
bottle.run(app, host='localhost', port=8080)