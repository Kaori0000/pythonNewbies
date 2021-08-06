from django.urls import path
from rango import views
from rango.views import AddCommentView


app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about_rango/', views.AboutRangoView.as_view(), name='about_rango'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('goto/', views.goto_url, name='goto'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('all_categories/',views.all_categories,name='all_categories'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('accounts/register/',views.MyRegistrationView.as_view(),
        name='registration_register'),
    
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('search/', views.search, name='search'),

    path('category/<slug:category_name_slug>/add_comment/',AddCommentView.as_view(),name ='add_comment'),
]