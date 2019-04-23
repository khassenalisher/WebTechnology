from rest_framework import serializers
from api.models import Task, TaskList

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        taskList = TaskList(**validated_data)
        taskList.save()
        return taskList

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    created = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    status = serializers.DateTimeField()

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance






class TaskModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs={
            'created_at':{'required':False},
            'due_on': {'required': False},
            'name': {'required': False},
            'task_list': {'required': False},
            'status': {'required': False}
        }

class TaskListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'
