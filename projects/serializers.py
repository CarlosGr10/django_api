from rest_framework import serializers
from .models import ModelProyect


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelProyect
        fields = ('id',
                'title',
                'description',
                'technology',
                'create_at')
        read_only_fields = ('create_at', )


# ========= NOTES =========
# read_only_fields, son campos que solo son lectura, no pueden actualizarce
