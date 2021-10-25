from rest_framework.serializers import ModelSerializer
from todo.models import ToDo

class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'description', 'done', 'created_at', 'updated_at')
