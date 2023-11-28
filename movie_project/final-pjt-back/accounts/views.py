from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny


# from django.db.models import Count

from .serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
)


User = get_user_model()


@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = ProfileSerializer(user)
    return Response(profile.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def follow(request, user_pk):
    profile_user = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    if me != profile_user:
        if me.followings.filter(pk=profile_user.pk).exists():
            me.followings.remove(profile_user)
        else:
            me.followings.add(profile_user)

    serializer = ProfileSerializer(profile_user)
    return Response(serializer.data)


