from django.urls import path
from . import views
from .templates.instrument import webapp

urlpatterns = [
    path('test1/', views.testOne, name='test1'),
    #path('$', webapp.button),
    path('showthis', webapp.showthis,name="script"),
]
