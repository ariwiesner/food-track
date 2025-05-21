from rest_framework import serializers
from .models import User, Hashtag, Place, Rating, ToVisitPlace, SharedAccess

class PlaceSerializer(serializers.ModelSerializer):
    added_by = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Place
        fields = '__all__'
       
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=15, write_only=True)
    username = serializers.CharField()
    added_places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
    
    def validate_password(self, value):
        if value.isnumeric():
            raise serializers.ValidationError("Password cannot be all numbers!")
        return value
    
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits!")
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits!")
        return value

    def create_user(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ToVisitPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToVisitPlace
        fields = '__all__'

class SharedAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedAccess
        fields = '__all__'