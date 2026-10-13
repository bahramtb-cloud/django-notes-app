from django.urls import path
from . import views
from . import api

urlpatterns = [
    path("", views.index),

    path("edit/<int:id>/", views.edit_note),

    path("delete/<int:id>/", views.delete_note),

    path("done/<int:id>/", views.done),

    path("profile/", views.profile),

    path("favorite/<int:id>/", views.favorite_note),

    path("export/", views.export_notes),

    path("http-test/", views.http_test),

    path("api/notes/", api.notes_api, name="notes_api"),

    path("api/notes/<int:note_id>/",api.note_detail_api,name="note_detail_api"),
    
]

