"""Web Routes."""

from masonite.helpers.routes import get, post
from app.http.controllers import BlogController

ROUTES = [
    get('/', 'BlogController@index'),
    get('/add', 'BlogController@add'),
    post('/add', 'BlogController@create'),
    get('/show/@id', 'BlogController@show'),
    get('/edit/@id', 'BlogController@edit'),
    post('/edit/@id', 'BlogController@update'),
    post('/delete', 'BlogController@delete'),
]
