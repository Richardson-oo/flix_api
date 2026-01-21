from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        # Permitir OPTIONS sempre
        if request.method == 'OPTIONS':
            return True
        if not hasattr(view, 'get_queryset'):
            return True

        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_suflix(method)
            return f'{app_label}.{action}_{model_name}'
        except Exception:
            return None

    def __get_action_suflix(self, method):
        method_action = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'HEAD': 'view'
        }
        return method_action.get(method, '')
