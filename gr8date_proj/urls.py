from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main Index Page
    path('', views.index, name='index'),
    
    # SEO Files
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
    
    # --- FIXED: Specific Legal & Support Routes (MUST BE ABOVE THE SLUG) ---
    path('about/', views.city_landing, {'city_slug': 'about'}, name='about'),
    path('privacy/', views.city_landing, {'city_slug': 'privacy'}, name='privacy'),
    path('terms/', views.city_landing, {'city_slug': 'terms'}, name='terms'),
    path('faq/', views.city_landing, {'city_slug': 'faq'}, name='faq'),
    path('contact/', views.city_landing, {'city_slug': 'contact'}, name='contact'),

    # Authentication Placeholders (Crucial for index.html links)
    path('login/', views.city_landing, {'city_slug': 'sydney'}, name='account_login'), 
    path('signup/', views.city_landing, {'city_slug': 'sydney'}, name='account_signup'),

    # --- THE DYNAMIC ROUTE (Must stay at the bottom) ---
    path('<slug:city_slug>/', views.city_landing, name='city_landing'),
]