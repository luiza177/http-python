import bottle
import word_counter
import json

app = bottle.Bottle()

@app.post('/contagem') # or @route('/login', method='POST')
def do_count_words():
    data = bottle.request.json
    text = data.get('text')
    if text is None:
        raise bottle.HTTPError(400)
    bottle.response.headers['Content-Type'] = 'application/json'
    return word_counter.word_analysis(text)

@app.error(404)
def error404(error):
    return 'Wrong number...tu tu tu tu'

@app.error(400)
def error400(error):
    return 'Bad request, check your headers and/or data'

bottle.run(app, host='localhost', port=8080)