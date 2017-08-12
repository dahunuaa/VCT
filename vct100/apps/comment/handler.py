# -*- coding:utf-8 -*-
from vct100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from vct100.libs.oauthlib import get_provider

class CommentListHandler(MultiStandardHandler,TokenHandler):
    _model = "comment.CommentHandler"
    enable_methods = ["post","get"]
    private = False

class CommentHandler(SingleStandardHanler,TokenHandler):
    _model = "comment.CommentHandler"
    enable_methods = ["get","delete"]
    private = False

handlers = [
    (r"",CommentListHandler,get_provider("comment")),
    (r"/(.*)",CommentHandler,get_provider("comment"))
]
