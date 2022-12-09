from rest_framework import serializers
from .models import Task

def starts_with_c(value):
    if value[0].lower() != 'c':
        raise serializers.ValidationError("Debe empezar con C")

def must_contains_numbers(value):
    if not any(char.isdigit() for char in value):
        raise serializers.ValidationError("Debe contener números")

class TaskSerializador(serializers.ModelSerializer):
    nombre = serializers.CharField(validators = [starts_with_c, must_contains_numbers])
    class Meta:
        model = Task
        fields = ('nombre', 'prioridad', 'completado_en')
    
    # def validate_prioridad(self, value):
    #     if value == None:
    #         return value
    #     if value < 1 or value > 3:
    #         raise serializers.ValidationError("Prioridad entre 1 y 3")
    #     return value

    def validate(self, data):
        prioridad = data.get('prioridad')
        if prioridad != None and (prioridad < 1 or prioridad > 3):
            raise serializers.ValidationError("Prioridad entre 1 y 3")
        # nombre = data.get('nombre')
        # if contains_number(nombre):
        #     raise serializers.ValidationError("Nombre no puede tener numeros")
        return data

def contains_number(string):
    return any(char.isdigit() for char in string)

# {"nombre": "tarea 6"}
# {"nombre": "tarea 6", "prioridad": 4}