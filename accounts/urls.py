from django.urls import path

from. import views

# naming the app a name
app_name = 'accounts'

urlpatterns =[
    path('signup/', views.signup, name='signup'),

]