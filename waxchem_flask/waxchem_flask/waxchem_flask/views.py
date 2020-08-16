"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from waxchem_flask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/mdhdb')
def contact():
    """Renders the contact page."""
    return render_template(
        'mdhdb.html',
        title='MDHDB',
        year=datetime.now().year,
        message='MDHDB page.'
    )

@app.route('/surface')
def about():
    """Renders the about page."""
    return render_template(
        'surface.html',
        title='Surface samples',
        year=datetime.now().year,
        message='Surface samples page.'
    )

@app.route('/collars')
def collars():

    return render_template(
        'collars.html',
        title='Collars',
        year=datetime.now().year,
        message='Collars page.'
    )