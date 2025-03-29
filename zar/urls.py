from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from category import views as cat_views
from post import views as post_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", cat_views.index, name="index"),
    path('add_post', login_required(post_views.add_post), name='add_post'),
    path('login', cat_views.login_view, name='login'),
    path('register', cat_views.login_view, name='register'),
    path('logout', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('category/<int:category_id>/', post_views.category_post_list, name='category_post_list'),
    path('post/<int:post_id>/', post_views.detail, name='post_detail'),  # Add this line
    path('admin/', admin.site.urls),
]

# Correct way to serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
