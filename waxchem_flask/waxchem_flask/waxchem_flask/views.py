"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from waxchem_flask import app
import pyodbc  

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/surface')
def about():
    """Renders the surface page."""
    return render_template(
        'surface.html',
        title='Surface samples',
        year=datetime.now().year,
        message='Surface samples page.'
    )

@app.route('/downhole')
def collars():
    """Renders the downhole page."""

    ## creating connection Object which will contain SQL Server Connection    
    #connection = pyodbc.connect('Driver={SQL Server};Server=nitro5;Database=drillholes;Trusted_Connection=yes; ')# Creating Cursor    
    connection = pyodbc.connect('Driver={SQL Server};Server=sqld\dev;Database=drillholes;Trusted_Connection=yes; ')# Creating Cursor    
 
    cursor = connection.cursor()    
    cursor.execute("SELECT top 15 * FROM Collar")    
    data = cursor.fetchall()
    connection.close() 

    return render_template(
        'downhole.html',
        title='Downhole samples',
        year=datetime.now().year,
        message='Downhole samples page.',
        data = data
    )

@app.route('/mdhdb')
def contact():
    """Renders the mdhdb page."""
    return render_template(
        'mdhdb.html',
        title='MDHDB',
        year=datetime.now().year,
        message='MDHDB page.'
    )
