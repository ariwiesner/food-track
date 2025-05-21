from . import views
from django.urls import path

urlpatterns = [
    # Users
    path("user/", views.add_user),
    path("users/", views.get_user),
    path("user/<int:id>/", views.get_specific_user),
    path("update_user/<int:id>/", views.update_user),
    path("delete_user/<int:id>/", views.delete_user),

    # Places
    path("place/", views.add_place),
    path("places/", views.get_palaces),
    path("place/<int:id>/", views.get_specific_place),
    path("update_place/<int:id>/", views.update_place),
    path("delete_place/<int:id>/", views.delete_place),

    # Rating
    path("rate/", views.add_rate),
    path("rates/", views.get_user),
    path("rate/<int:id>/", views.get_specific_rate),
    path("update_rate/<int:id>/", views.update_rate),
    path("delete_rate/<int:id>/", views.delete_rate),

    # Hashtags
    path("hashtag/", views.add_hashtag),
    path("hashtags/", views.get_hashtags),
    path("hashtag/<int:id>/", views.get_specific_hashtag),
    path("update_hashtag/<int:id>/", views.update_hashtag),
    path("delete_hashtag/<int:id>/", views.delete_hashtag),

    # To visit place
    path("to_visit_place/", views.add_to_visit_place),
    path("to_visit_places/", views.get_to_visit_places),
    path("to_visit_place/<int:id>/", views.get_specific_to_visit_place),
    path("update_to_visit_place/<int:id>/", views.update_to_visit_place),
    path("delete_to_visit_places/<int:id>/", views.delete_to_visit_place),

    # Shared access
    path("shared_access/", views.add_shared_access),
    path("all_shared_access/", views.get_all_shared_access),
    path("shared_access/<int:id>/", views.get_specific_shared_access),
    path("update_shared_access/<int:id>/", views.update_shared_access),
    path("delete_shared_access/<int:id>/", views.delete_shared_access),
]