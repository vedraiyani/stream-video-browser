#https://flask.palletsprojects.com/en/1.1.x/api/#stream-helpers
from flask import stream_with_context, request, Response
from flask import Flask
import time 

app = Flask(__name__)

@app.route('/stream')
def streamed_response():
    @stream_with_context
    def generate():
        time.sleep(1)
        yield 'Hello '
        time.sleep(1)
        yield request.args['name']
        time.sleep(1)
        yield '!'
    return Response(generate())

# start the flask app
app.run(host='0.0.0.0', port='8000', debug=True,
    threaded=True, use_reloader=False)