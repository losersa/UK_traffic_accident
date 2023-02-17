# -*- coding: UTF-8 -*- #
"""
@filename:urls.py
@author:Gxr
@time:2023-02-08
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /users/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /users/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /users/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('404', views.error_404, name='404'),
    path('account', views.account, name='account'),
    path('charts', views.charts, name='charts'),
    path('docs', views.docs, name='docs'),
    path('help', views.help, name='help'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('notifications', views.notifications, name='notifications'),
    path('orders', views.orders, name='orders'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),

]