from flask import Blueprint, render_template, request
from models import Company

from syncSearchEngine import client

companyBluePrint =  Blueprint('company', __name__)


@companyBluePrint.route("/company")
def indexPage():
    activePage = "company"

    sortColumn = request.args.get('sortColumn', 'name')
    if sortColumn == 'namn':
        sortColumn = 'name'
    sortOrder = request.args.get('sortOrder', 'asc')
    page = int(request.args.get('page', 1))

    searchWord = request.args.get('q','*')

    skip = (page-1) * 10
    result = client.search(search_text=searchWord,
        include_total_count=True,skip=skip,
        top=10,
        order_by=sortColumn + ' '  + sortOrder )

    alla = result
    return render_template('company/list.html', companies=alla)


@companyBluePrint.route("/company/<id>")
def companyPage(id):
    activePage = "company"
    return "a"

