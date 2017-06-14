from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import MasterDetailView
from flask_appbuilder import ModelView, AppBuilder
from .models import About, News, Publication, Activity, Message, Media
from app import appbuilder, db
from flask_appbuilder.widgets import ListThumbnail, ListAddWidget, FormInlineWidget, ListMasterWidget, ListItem


class MediaView(ModelView):

    datamodel = SQLAInterface(Media)

    list_widget = ListThumbnail

    list_columns = ['photo_img_thumbnail']


    add_fieldsets = [
        ('Media', {'fields': ['photo', 'publications', 'name']})
    ]

    edit_fieldsets = [
        ('Media', {'fields': ['publications', 'news']})
    ]

class MyMediaView(ModelView):
    datamodel = SQLAInterface(Media)
    add_template = 'media_add.html'
    static_folder = 'static/appbuilder'


class AboutView(ModelView):
    datamodel = SQLAInterface(About)



class NewsView(ModelView):
    datamodel = SQLAInterface(News)

    # list_columns = ['name','posted_date', 'media']
    add_columns = ['name', 'body', 'media']
    # label_columns = {'name':'News Title', 'posted_date':'Posted On', 'media':'Gallery'}
    related_views = [MyMediaView]


class PublicationView(ModelView):

    datamodel = SQLAInterface(Publication)
    list_widget = ListItem

    list_columns = ['photo_img_thumbnail', 'name', 'published_date']
    related_views = [MediaView]
    # add_fieldsets = [
    #     ('Media', {'fields': ['Media.photo']})
    # ]



class ActivityView(ModelView):
    datamodel = SQLAInterface(Activity)
    list_columns = ['name', 'start_date', 'end_date']
    related_views = [MediaView]
    list_widget = ListThumbnail



class MessageView(ModelView):

    datamodel = SQLAInterface(Message)
    list_columns = ['name', 'posted']
    related_views = [MediaView]
    list_widget = ListThumbnail



db.create_all()

appbuilder.add_view(AboutView, "About", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(PublicationView, "Publications", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(ActivityView, "Activities", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MessageView, "Messages", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MediaView, "Media", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MyMediaView, "MyMedia", icon="fa-folder-open-o", category="Admin")




"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404




