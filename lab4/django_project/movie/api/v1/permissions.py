from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        print("inside permission")
        for grp in request.user.groups.all():
            print(grp)

        if request.user.groups.filter(name='developer').exists():
            print('Has Group')
            return False
        return True
