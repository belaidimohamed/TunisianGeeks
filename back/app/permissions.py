from rest_framework import permissions


class IsOwner(permissions.BasePermission):
	def has_permission(self, request, view):
		print("\n onee : " ,request.user,request.user.is_authenticated, "\n")
		return request.user and request.user.is_authenticated
	def has_object_permission(self, request, view, obj):
		print("\n two : " ,obj.user,request.user, '\n')
		print(obj)
		return obj.user == request.user