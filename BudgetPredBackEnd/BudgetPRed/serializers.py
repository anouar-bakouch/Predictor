from django.shortcuts import get_object_or_404
from rest_framework import serializers
from BudgetPRed.models import Budget, User

class BudgetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Budget
        fields = ('IDEIMPST', 'MONTSTRU', 'MONTRAPP', 'MOISSOLD', 'CODTYPAC', 'LIBACTGE', 'Budgets', 'User', 'budgetPhoto')
        
    # create method to create a new budget 
    def create(self, validated_data):
        return Budget.objects.create(**validated_data)
    
    # update method to update an existing budget
    def update(self, instance, validated_data):
        instance.IDEIMPST = validated_data.get('IDEIMPST', instance.IDEIMPST)
        instance.MONTSTRU = validated_data.get('MONTSTRU', instance.MONTSTRU)
        instance.MONTRAPP = validated_data.get('MONTRAPP', instance.MONTRAPP)
        instance.MOISSOLD = validated_data.get('MOISSOLD', instance.MOISSOLD)
        instance.CODTYPAC = validated_data.get('CODTYPAC', instance.CODTYPAC)
        instance.LIBACTGE = validated_data.get('LIBACTGE', instance.LIBACTGE)
        instance.Budgets = validated_data.get('Budgets', instance.Budgets)
        instance.User = validated_data.get('User', instance.User)
        instance.budgetPhoto = validated_data.get('budgetPhoto', instance.budgetPhoto)
        instance.save()
        return instance
    
    # delete method to delete an existing budget
    def delete(self, instance):
        instance.delete()
        return instance
    
    # get method to get an existing budget
    def get(self, instance):
        return instance
    
    # get all method to get all existing budgets
    def get_all(self):
        return Budget.objects.all()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TokenPairSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

