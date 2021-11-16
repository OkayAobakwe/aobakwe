from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	path('blog/', views.blog, name='blog'),
	path('blog/<int:entry_id>/', views.entry, name='entry'),
]