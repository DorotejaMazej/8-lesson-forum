#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAdd, TopicDetails, DeleteTopic
from handlers.comments import CommentAdd
from handlers.workers.email_comment_worker import EmailNewComment

app = webapp2.WSGIApplication({
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAdd, name="topic_add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', DeleteTopic, name="delete-topic"),

    # tasks
    webapp2.Route('/task/email-new-comment', EmailNewComment)
}, debug=True)
