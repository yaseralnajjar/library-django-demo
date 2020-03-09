from rest_framework.permissions import BasePermission


class IsBookAuthor(BasePermission):

    def has_object_permission(self, request, view, book):
        return request.user.id == book.author.id
