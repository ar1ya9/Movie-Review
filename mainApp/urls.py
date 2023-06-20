from django.urls import path
from . import views

app_name='mainApp'

urlpatterns = [
    path('',views.home,name='home'),
    path('d/<int:id>/',views.details, name='details'),
    path('admovie',views.addmovie,name='addmovie'),
    path('editmovie/<int:id>/',views.editmovie,name='editmovie'),
    path('demovie/<int:id>/',views.deletemovie,name='deletemovie'),
    path('adreview/<int:id>/',views.adreview,name='addreview'),
    path('edreview/<int:movie_id>/<int:review_id>/', views.edreview, name='editreview'),
    path('dereview/<int:movie_id>/<int:review_id>/', views.dereview, name='deletereview'),

]