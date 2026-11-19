from rest_framework import generics, mixins
from .models import Teachers
from .serializers import TeachersSerializer
class TeachersListView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class TeachersDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk=pk)
    def put(self, request, pk):
        return self.update(request, pk=pk)
    def patch(self, request, pk):
        return self.partial_update(request, pk=pk)
    def delete(self, request, pk):
        return self.destroy(request, pk=pk)