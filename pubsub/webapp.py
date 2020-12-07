#!/usr/bin/env python3

## Using Bottle to Build REST APIs and Web Applications
# Bottle is a typical, modern, mico web framework (similar frameworks are Flask or Django)
# Core Skills: routing, requests, responses, templating
# Learn to implement content negotiation, cache controls, and cookies
#
# HINT: With vim slime, you have to send the whoel buffer or file to REPL. See [200~https://github.com/jpalardy/vim-slime/issues/216 how to do this

from bottle import Bottle, get, run, post, view, abort
from bottle import response, request, template, static_file
from pprint import pprint
from typing import Dict, Optional
import time
import secrets
import algebra
import os

secret = 'the life expectancy of a lannister stark or targaryen is short'
app = Bottle()

User = str
logged_in_users: Dict[bytes, User] = {}

@app.route('/')
def welcome():
    # whenever you do content negotiation with caching, set a Vary header
    response.set_header('Vary', 'Accept')
    pprint(dict(request.headers))
    # content negotiation: does the server send the data the client requests?
    # e.g. browsers will preferably request HTML
    # whereas curl will request plain text
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'
    return 'Hello'

@app.route('/now')
def time_service():
    response.content_type = 'text/plain'
    # caching the time_service function to 1 second.
    # This means that even if 100,000 users want to get the time, the result from the first call is used for 1 second (age), so every call afterwards gets answered by the cached result
    response.set_header('Cache-Control', 'max-age=1')
    return time.ctime()

@app.route('/upper/<word>')
def upper_word(word):
    response.content_type = 'text/plain'
    return word.upper()

@app.route('/area/circle')
def circle_area_service():
    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    print(f'Last visit: {last_visit}')
    response.set_cookie('last-visit', time.ctime(), secret=secret)
    response.set_header('Vary', 'Accept')
    pprint(dict(request.query)) # query is like .../circle?radius=10.0
    # radius=abc would result in Error: 500 (Internal Server Error)
    # Users shall never see this error because it means that something went wrong in your application
    # We see the error traceback in the console
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]
    # area = algebra.area_circle(radius) -> that gave an NameError: name 'algebra' is not defined
    # dont do this, because we want to separate web server and functionality
    area = float(3.14159 * radius ** 2.0)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return f'<p> The area is <em> {area} </em> </p>'
    # return dict which convertes to JSON in case we call service from e.g. curl
    # also include service (REST API best practice for debugging
    return dict(radius=radius, area=area, service=request.path)

### File Server ###
file_template = ''' \
<h1> List of files in <em> Congress Data </em> directory </h1>
<hr>
<ol>
    % for file in files:
        <li> <a href="files/{{file}}"> {{file}} </a> </li>
    % end
</ol>
'''

@app.route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir('congress_data')
    if 'text/html' not in request.headers.get('Accept', '*/*'):
        return dict(files=files)
    return template(file_template, files=files)

@app.route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, './congress_data')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
