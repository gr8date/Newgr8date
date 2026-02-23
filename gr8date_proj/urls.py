from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main Index Page
    path('', views.index, name='index'),
    
    # SEO Files: Served directly from your templates folder
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
    
    # Authentication Placeholders (Points to Sydney landing for now)
    path('login/', views.city_landing, {'city_slug': 'sydney'}, name='account_login'), 
    path('signup/', views.city_landing, {'city_slug': 'sydney'}, name='account_signup'),

    # THE DYNAMIC ROUTE: This handles all cities AND all legal pages (about, privacy, terms, faq, contact)
    # This must remain at the bottom of the list.
    path('<slug:city_slug>/', views.city_landing, name='city_landing'),
]

