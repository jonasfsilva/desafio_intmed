from django.contrib import admin
from django.urls import path
from django.urls import include
from .routers import router
from django.contrib.auth import views
from trello_app.views import WebHookTrelloView

login = views.LoginView.as_view(template_name='rest_framework/login.html')
login_kwargs = {}
logout = views.LogoutView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('webhook-trello/', WebHookTrelloView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path(r'', login, login_kwargs, name='login'),
    path(r'logout/', logout, name='logout'),
]