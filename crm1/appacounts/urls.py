from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user'),

    path('account/',views.accountSettings, name='account'),

    path('products/', views.products, name="products"),
    path('custumers/<str:pk_test>/', views.custumers, name="custumer"),

    path('create_order/<str:pk>/', views.createOrder, name='create_order'), 
    path('update_order/<str:pk>/', views.updateorder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder, name='delete_order'),

    path('resert_password/', auth_views.PasswordResetView.as_view(template_name = 'appacounts/password_reset.html'), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
