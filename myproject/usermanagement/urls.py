from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('admin/softdelete/<int:user_id>/', views.soft_delete_user, name='soft_delete_user'),
    path('admin/adduser/', views.add_user,name="add_user"),
    path('admin/logout',views.admin_logout,name="admin_logout")
]