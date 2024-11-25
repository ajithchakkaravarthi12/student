from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index", views.index_page, name="index"),
    path("display", views.display_page, name="display"),
    path("delete/<int:id>", views.delete_data, name="delete_data"),  # Pass 'id'
    path("update/<int:id>", views.update_data, name="update_data"),  # Pass 'id'
]
