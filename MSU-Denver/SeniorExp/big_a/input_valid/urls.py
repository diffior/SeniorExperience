from django.urls import path
#from .views import main, second_in
from .views import *

urlpatterns = [
    path('', inputValidation.main),
    path('second', inputValidation.second_in),
    path('host', inputValidation.host),
    path('state', inputValidation.state),
    path('namesubject', inputValidation.namesubject),
    path('port', inputValidation.port),
    path('email', inputValidation.email),
    path('bodymsg', inputValidation.bodymsg),
    path('command', inputValidation.command),
    path('count', inputValidation.count),
    path('unit', inputValidation.unit),
    path('timespec', inputValidation.timespec),
    path('repo', inputValidation.repo),
    path('dest', inputValidation.dest)
]
