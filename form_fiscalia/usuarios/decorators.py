from django.contrib.auth.decorators import user_passes_test

def group_required(group_name):
    """Permite el acceso solo a usuarios de cierto grupo."""
    def in_group(u):
        return u.is_authenticated and u.groups.filter(name=group_name).exists()
    return user_passes_test(in_group)
