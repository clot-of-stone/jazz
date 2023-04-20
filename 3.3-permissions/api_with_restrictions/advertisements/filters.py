from django_filters import rest_framework as filters

from .models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'creator', 'created_at']
