from flask import Flask


from flask_caching import Cache
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object

app.config.from_object('config.DevelopmentConfig')



cache = Cache(app)





@app.route('/cache/<country>/<capital>')
def cache_set(country, capital):

    cache.set(country,{'country':capital})
    return 'Done'

@app.route('/cache/<country>')
def cache_get(country):
    resp = cache.get(country)
    print(resp)
    if resp is not None:
        return cache.get(country)
    else:
        return 'None'


if __name__ == "__main__":
    app.run()
