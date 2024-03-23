from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Follow, CustomUser, Profile


class UserAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password_confirm', 'email', 'phone_number')
        extra_kwargs = {
            'phone_number': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return CustomUser.objects.create_user(**validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name','phone_number']




class FollowingSerializer(serializers.ModelSerializer):
    following_username = serializers.ReadOnlyField(source='following.username')
    class Meta:
        model = Follow
        fields = ['id','follower' ,'following', 'following_username', 'created_at']
        read_only_fields = ['follower']
class FollowerSerializer(serializers.ModelSerializer):
    follower_username = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'follower_username', 'created_at']
        read_only_fields = ['follower']

    def get_follower_username(self, instance):
        return instance.follower.username

    









class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.SerializerMethodField()
    following_username = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['id','follower_username', 'following','following_username', 'created_at']

    def get_follower_username(self, instance):
        return instance.follower.username
    
    def get_following_username(self, instance):
        return instance.following.username
class PublicProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'profile_picture')



class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_picture', 'is_public']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user and not request.user.is_staff:
            try:
                profile_instance = request.user.profile
                self.fields['user'].queryset = CustomUser.objects.filter(pk=profile_instance.user.pk)
            except Profile.DoesNotExist:
                pass



    

    