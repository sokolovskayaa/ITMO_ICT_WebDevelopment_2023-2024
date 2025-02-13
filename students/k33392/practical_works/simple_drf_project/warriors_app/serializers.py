from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class WarriorWithProfessionsSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        exclude = ['skill']


class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        exclude = ['profession']
