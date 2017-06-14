from flask import url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from markupsafe import Markup
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
import datetime


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class Media(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=True)
    # path = Column(String(250), unique=True, nullable=True)
    photo = Column(ImageColumn(thumbnail_size=(30, 30, True), size=(300, 300, True)))
    # posted = Column(Date, default=today, nullable=False)
    publications = relationship("Publication")
    publications_id = Column(Integer, ForeignKey('publication.id'), nullable=True)
    news = relationship("News")
    news_id = Column(Integer, ForeignKey('news.id'), nullable=True)
    activities = relationship("Activity")
    activities_id = Column(Integer, ForeignKey('activity.id'), nullable=True)
    messages = relationship("Message")
    messages_id = Column(Integer, ForeignKey('message.id'), nullable=True)

    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('MediaView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="' + im.get_url(self.photo) + \
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('MediaView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('MediaView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) + \
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('MediaView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def __repr__(self):
        return self.name



class About(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    body = Column(Text(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class News(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    body = Column(Text(50), unique=True, nullable=False)
    posted_date = Column(Date, default=today, nullable=False)
    media = relationship('Media')

    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('NewsModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="' + im.get_url(self.photo) + \
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('NewsModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('NewsModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) + \
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('NewsModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def __repr__(self):
        return self.name

class Publication(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    body = Column(Text(50), unique=True, nullable=False)
    published_date = Column(Date, default=today, nullable=False)

    def __repr__(self):
        return self.name

class Activity(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    body = Column(Text(50), unique=True, nullable=False)
    start_date = Column(Date, default=today, nullable=False)
    end_date = Column(Date, nullable=True)

    def __repr__(self):
        return self.name

class Message(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    body = Column(Text(50), unique=True, nullable=False)
    posted = Column(Date, default=today, nullable=False)


    def __repr__(self):
        return self.name

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
