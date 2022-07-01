from django.shortcuts import get_object_or_404
from rest_framework import permissions

from review.models import Review
from user.models import User

class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.user.is_authenticated)

class DeleteReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        review = get_object_or_404(Review, id=view.kwargs["review_id"])
       
        critic = User.objects.get(id=review.critic_id)
        
        if request.user.id != critic.id and not request.user.is_superuser:
            return False

        return (request.user.is_authenticated or request.user.is_superuser)