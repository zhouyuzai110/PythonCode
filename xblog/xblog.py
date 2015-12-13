#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 
import os
from flask import Flask, flash, redirect, url_for, render_template, session, request
import redis

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

SECRET_KEY = 'you-will-never-guess'
DEBUG = True

app = Flask('__name__')
app.config.from_object(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    rd = redisconn()
    blogs = rd.lrange('bloglist',0,-1)
    return render_template('base.html', blogs = blogs)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if check_zhanghao():
            session['logined'] = True
            flash('welcome login')
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        rd = redisconn()
        rd.set(request.form['username'],request.form['password'])    
        flash('register is successful')
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/post', methods = ['GET', 'POST'])
def post():
    if request.method == 'POST':
        rd = redisconn()
        
        rd.set(request.form['title'],request.form['content'])
        rd.lpush('bloglist',request.form['title'])
        flash('new post is ok')
        return redirect(url_for('index'))    
    return render_template('post.html')    


@app.route('/show_blog=<title>', methods = ['GET'])
def show_blog(title):
    rd = redisconn()
    ff = rd.get(title)
    return render_template('show_blog.html', title = title ,content = ff) 


@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('logined')
    return redirect(url_for('index')) 

@app.route('/del', methods = ['GET', 'POST'])
def delitem():
    rd = redisconn()
    rd.delete(request.form['title'])
    rd.lrem('bloglist', request.form['title'])
    flash('del post is ok')
    return redirect(url_for('index'))

@app.route('/req', methods = ['GET'])
def req():
    return render_template('req.html', keys = dir(request)) 


def check_zhanghao():
    rd = redisconn()
    if request.form['password'] != rd.get(request.form['username']):
       return False
    else:
        return True

def redisconn():
    r = redis.Redis(host='localhost',port=6379,db=0)
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0')
