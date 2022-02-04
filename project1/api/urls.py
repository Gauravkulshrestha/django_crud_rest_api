from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path("", views.createItem, name="home"),
    path("updateitem/<int:id>/", views.updateItem, name="update-item"),
    path("deleteitem/<int:id>/", views.deleteItem, name="delete-item"),
    path("api/", views.getRoutes, name="routes"),
    path("api/item-list/", views.all_Items, name="routes"),
    path("api/create-item/", views.create_Items, name="api-create-item"),
    path("api/update-item/<int:id>/", views.update_Items, name="api-update-item"),            
    path("api/delete-item/<int:id>/", views.delete_Items, name="api-delete-item"),
]