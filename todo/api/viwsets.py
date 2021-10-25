from rest_framework.viewsets import ModelViewSet
from todo.models import ToDo
from .serializers import ToDoSerializer
from rest_framework.filters import SearchFilter


class AccountViewSet(ModelViewSet):
    serializer_class = ToDoSerializer

    filter_backends = (SearchFilter,)
    search_fields = ('id',)
    lookup_field = 'id'

    def get_queryset(self):
        done = self.request.query_params.get('done', None)
        queryset = ToDo.objects.all()
        if done:
            queryset = ToDo.objects.filter(done=done)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(AccountViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(AccountViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(AccountViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(AccountViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(AccountViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(AccountViewSet, self).partial_update(request, *args, **kwargs)
