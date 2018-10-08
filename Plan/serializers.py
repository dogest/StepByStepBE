from rest_framework import serializers

from Plan.models import Plan


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'area', 'name')
