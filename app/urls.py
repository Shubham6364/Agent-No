import imp
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app.urls'))
      path('', views.home,name='home'),
      path('post/', views.post,name="post"),
      path('rent/', views.rent,name='rent'),
      path('sign' , views.sign,name='sign'),
      path('form/' , views.databasesave),
      path('login/',views.loginpage,name='login'),
      # path('logout/', views.handlelogout, name='handlelogout'),
      path('main/', views.main,name='main'),
      path(r'detail/<slug>', views.detail,name='detail'),
      path('rentdetail/<detailid1id>', views.rentdetail,name='rentdetail'),
      # path('multiple/', views.multiple,name='multiple'),
      path('search', views.search,name="search"),
      path('logout', views.logout,name="logout"),
      path('dashboard', views.dashboard,name="dashboard"),
      path('stafflogin',views.stafflogin,name='stafflogin'),
      path('staffsignup',views.staffsign,name='staffsignup'),
      path('salecrud',views.salecrud,name='salecrud'),
      path('stafflogout',views.stafflogout,name='stafflogout'),
      path('delete/<str:id>',views.delete,name='delete'),
      path('UserProfile',views.UserProfile,name='UserProfile'),
      path('rentcrud',views.rentcrud,name='rentcrud'),
      path('upload/',views.upload,name='upload'),
      path('delete<str:id>',views.delete,name="delete"),
      

 ]