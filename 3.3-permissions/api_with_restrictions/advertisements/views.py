from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement, Favourite
from .serializers import AdvertisementSerializer


class GetAccessPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.user.is_superuser


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Advertisement.objects.filter(
                creator=self.request.user, draft=True) | \
                       Advertisement.objects.filter(draft=False)
        else:
            queryset = Advertisement.objects.filter(draft=False)
        return queryset

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['destroy', 'update', 'partial_update']:
            return [GetAccessPermission()]
        return []

    @action(detail=True, methods=['POST'], url_path=r'fav')
    def fav(self, request, pk=None):
        advertisement = self.get_object()
        advertisement_in_favourites = Favourite.objects.filter(
            user=self.request.user).filter(
            advertisement=advertisement.id)

        if advertisement.draft:
            raise ValidationError({
                'error': 'Нельзя добавить черновик в избранные'
            })

        if advertisement_in_favourites.exists():
            raise ValidationError({
                'error': 'Это объявление уже в избранном'
            })

        if advertisement.creator == self.request.user:
            return Response({
                'status': 'Нельзя добавить собственное объявление в избранные'
            })

        advertisement.favourite.add(self.request.user)
        advertisement.save()
        return Response({
            'status': f'Объявление #{advertisement.id} было добавлено в '
                      f'избранные'
        })
