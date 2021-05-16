from django_filters import rest_framework as filters

from .models import Post


class GroupFilter(filters.FilterSet):
    group = filters.CharFilter(field_name='group__id')

    class Meta:
        model = Post
        fields = ['group']
