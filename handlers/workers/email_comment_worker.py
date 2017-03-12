from handlers.base import BaseHandler
from google.appengine.api import mail


class EmailNewComment(BaseHandler):
    def post(self):
        topic_author_email = self.request.get("topic.author_email")
        topic_title = self.request.get("topic_title")
        comment_content = self.request.get("comment_content")

        mail.send_mail(sender="teja.mazej@gmail.com",
                       to=topic_author_email,
                       subject="Dobil/a si nov komentar v topicu %s!" % topic_title,
                       body="Nov komentar: {0}".format(comment_content))



