from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Heckles'} 
    posts = [ #fake array of posts
        {
            'author': {'nickname': 'Johnnie'},
            'body': 'Beautiful day in Bend!'
        },
        {
            'author': {'nickname': 'Salsburry'},
            'body': 'Oh the day when the gravy dries up!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
