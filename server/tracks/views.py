from server.abstract_models import abstractFunctions
from django.views.decorators.csrf import csrf_exempt
from tracks.models import User, Place, Rating, Hashtag, ToVisitPlace, SharedAccess
from tracks.serializer import UserSerializer, PlaceSerializer, RatingSerializer, HashtagSerializer, ToVisitPlaceSerializer, SharedAccessSerializer

# User
@csrf_exempt
def add_user(request):
    return abstractFunctions.add(request, UserSerializer)

@csrf_exempt
def get_user(request):
    return abstractFunctions.get(request, User, UserSerializer)

@csrf_exempt
def get_specific_user(request, id):
    return abstractFunctions.get(request, User, UserSerializer, id)

@csrf_exempt
def update_user(request, id):
    return abstractFunctions.update(request, User, UserSerializer, id)

@csrf_exempt
def delete_user(request, id):
    return abstractFunctions.delete(request, User, id)

#######################################################################################################
   
# Place
@csrf_exempt
def add_place(request):
    return abstractFunctions.add(request, PlaceSerializer)

@csrf_exempt
def get_palaces(request):
    return abstractFunctions.get(request, Place, PlaceSerializer)

@csrf_exempt
def get_specific_place(request, id):
    return abstractFunctions.get(request, Place, PlaceSerializer, id)

@csrf_exempt
def update_place(request, id):
    return abstractFunctions.update(request, Place, PlaceSerializer, id)

@csrf_exempt
def delete_place(request, id):
    return abstractFunctions.delete(request, Place, id)

#######################################################################################################

# Rating
@csrf_exempt
def add_rate(request):
    return abstractFunctions.add(request, RatingSerializer)

@csrf_exempt
def get_rates(request):
    return abstractFunctions.get(request, Rating, RatingSerializer)

@csrf_exempt
def get_specific_rate(request, id):
    return abstractFunctions.get(request, Rating, RatingSerializer, id)

@csrf_exempt
def update_rate(request, id):
    return abstractFunctions.update(request, Rating, RatingSerializer, id)

@csrf_exempt
def delete_rate(request, id):
    return abstractFunctions.delete(request, Rating, id)

#######################################################################################################

# Hashtag
@csrf_exempt
def add_hashtag(request):
    return abstractFunctions.add(request, HashtagSerializer)

@csrf_exempt
def get_hashtags(request):
    return abstractFunctions.get(request, Hashtag, HashtagSerializer)

@csrf_exempt
def get_specific_hashtag(request, id):
    return abstractFunctions.get(request, Hashtag, HashtagSerializer, id)

@csrf_exempt
def update_hashtag(request, id):
    return abstractFunctions.update(request, Hashtag, HashtagSerializer, id)

@csrf_exempt
def delete_hashtag(request, id):
    return abstractFunctions.delete(request, Hashtag, id)

#######################################################################################################

# To visit
@csrf_exempt
def add_to_visit_place(request):
    return abstractFunctions.add(request, ToVisitPlaceSerializer)

@csrf_exempt
def get_to_visit_places(request):
    return abstractFunctions.get(request, ToVisitPlace, ToVisitPlaceSerializer)

@csrf_exempt
def get_specific_to_visit_place(request, id):
    return abstractFunctions.get(request, ToVisitPlace, ToVisitPlaceSerializer, id)

@csrf_exempt
def update_to_visit_place(request, id):
    return abstractFunctions.update(request, ToVisitPlace, ToVisitPlaceSerializer, id)

@csrf_exempt
def delete_to_visit_place(request, id):
    return abstractFunctions.delete(request, ToVisitPlace, id)

#######################################################################################################

# Shared access
@csrf_exempt
def add_shared_access(request):
    return abstractFunctions.add(request, SharedAccess)

@csrf_exempt
def get_all_shared_access(request):
    return abstractFunctions.get(request, SharedAccess, SharedAccessSerializer)

@csrf_exempt
def get_specific_shared_access(request, id):
    return abstractFunctions.get(request, SharedAccess, SharedAccessSerializer, id)

@csrf_exempt
def update_shared_access(request, id):
    return abstractFunctions.update(request, SharedAccess, SharedAccessSerializer, id)

@csrf_exempt
def delete_shared_access(request, id):
    return abstractFunctions.delete(request, SharedAccess, id)

