from django.urls import path
from rango import views


app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    #path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    #path('restricted/', views.restricted, name='restricted'),
    #path('logout/', views.user_logout, name='logout'),

    path('profile_register/', views.register_profile, name='profile_register'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('accounts/register/',views.MyRegistrationView.as_view(),
        name='registration_register'),
]