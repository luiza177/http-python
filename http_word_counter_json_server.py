import bottle
import word_counter
import json

app = bottle.Bottle()

@app.post('/contagem') # or @route('/login', method='POST')
def do_count_words():
    try:
        data = bottle.request.json
        if data is None:
            raise ValueError
        try:
            text = data['text']
        except:
            raise KeyError
        if text is None:
            raise ValueError
    except (ValueError, KeyError):
        bottle.response.status = 400
        return
    bottle.response.headers['Content-Type'] = 'application/json'
    return word_counter.word_analysis(text)


bottle.run(app, host='localhost', port=8080)