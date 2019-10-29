from flask import jsonify
from flask import request

from app.forms.book import SearchForms
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from . import web


@web.route('/book/search')
def search():
    form = SearchForms(request.args)

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)