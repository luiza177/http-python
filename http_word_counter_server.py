import bottle
import word_counter


app = bottle.Bottle()

@app.get('/contagem')
def get_text():
    return '''
        <form action="/contagem" method="post">
            Text: </br>
            <textarea cols="100" rows="20" name="form_text">Enter your text.</textarea></br>
            <input value="Submit!" type="submit" />
        </form>
    '''

@app.post('/contagem') # or @route('/login', method='POST')
def do_count_words():
    form_text = bottle.request.forms.get('form_text')
    words = word_counter.word_analysis(form_text)
    return word_counter.display_word_analysis(words)


bottle.run(app, host='localhost', port=8080)