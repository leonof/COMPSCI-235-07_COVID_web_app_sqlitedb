from flask import Blueprint, render_template
from datetime import datetime
from flask import Flask,request
import math
import covid.adapters.repository as repo
from covid.adapters.repository import AbstractRepository

home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/')
def index():
    numsInPage = 5;
    movieList = []
    param_dict = {}
    page = int(request.args.get("pagenum",1))
    searchKey = request.args.get("search",'')
    for m in repo.repo_instance.getAllMovie():
        print(m.__dict__)
        thisTitle = str(m.__dict__['__title'])
        thisYear = str(m.__dict__['__year'])
        thisDescription = str(m.__dict__['__description'])
        thisRuntime = str(m.__dict__['__runtime'])
        if searchKey in thisTitle or searchKey == thisYear or searchKey in thisDescription:
            movieList.append(m)
    param_dict['page'] = page
    param_dict['searchKey'] = searchKey
    param_dict['pageAll'] = math.ceil(len(movieList)/numsInPage)
    param_dict['movie'] = ''
    movieBegin = (page-1)*numsInPage
    movieEnd = page*numsInPage
    if movieBegin > len(movieList)-1:
        movieBegin = len(movieList)-numsInPage
        movieEnd = len(movieList)
    elif movieEnd > len(movieList)-1:
        movieEnd = len(movieList)
    for m in range(movieBegin,movieEnd):
        thisTitle = str(movieList[m].__dict__['__title'])
        thisYear = str(movieList[m].__dict__['__year'])
        thisDescription = str(movieList[m].__dict__['__description'])
        thisRuntime = str(movieList[m].__dict__['__runtime'])
        thisText = thisTitle+';;'+thisYear+';;'+thisRuntime+';;'+thisDescription+';;;'
        param_dict['movie'] = param_dict['movie']+thisText
    return render_template('index.html', param_dict=param_dict)

@home_blueprint.route('/search/')
def search():
    numsInPage = 5;
    movieList = []
    param_dict = {}
    page = int(request.args.get("pagenum",1))
    searchKey = request.args.get("search",'')
    for m in getAllMovie():
        thisTitle = str(m.title)
        thisYear = str(m.year)
        thisDescription = str(m.description)
        #thisRuntime = str(m.runtime_minutes)
        if searchKey in thisTitle or searchKey in thisYear or searchKey in thisDescription:
            movieList.append(m)
    param_dict['page'] = page
    param_dict['searchKey'] = searchKey
    param_dict['pageAll'] = math.ceil(len(movieList)/numsInPage)
    param_dict['movie'] = ''
    movieBegin = (page-1)*numsInPage
    movieEnd = page*numsInPage
    if movieBegin > len(movieList)-1:
        movieBegin = len(movieList)-numsInPage
        movieEnd = len(movieList)
    elif movieEnd > len(movieList)-1:
        movieEnd = len(movieList)
    for m in range(movieBegin,movieEnd):
        thisTitle = str(movieList[m].__dict__['__title'])
        thisYear = str(movieList[m].__dict__['__year'])
        thisDescription = str(movieList[m].__dict__['__description'])
        thisRuntime = str(movieList[m].__dict__['__runtime'])
        thisText = thisTitle+';;'+thisYear+';;'+thisRuntime+';;'+thisDescription+';;;'
        param_dict['movie'] = param_dict['movie']+thisText
    return render_template('index.html', param_dict=param_dict)
