from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = PontoTuristicoSerializer
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    ###metodos drf a sobescrever###

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'hello': request.data})

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    ## to do the default behavior of http verb
    #     return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass