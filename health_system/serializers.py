from rest_framework import serializers
from .models import Client, Enrollment, HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name']

class EnrollmentSerializer(serializers.ModelSerializer):
    program = HealthProgramSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['program', 'date_enrolled']

class ClientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'email', 'phone']

    def get_full_name(self, obj):
        names = [obj.first_name, obj.middle_name, obj.last_name]
        return " ".join(name for name in names if name)  

    def get_enrollments(self, obj):
        enrollments = Enrollment.objects.filter(client=obj)
        return EnrollmentSerializer(enrollments, many=True).data




from rest_framework import serializers
from .models import Client, Enrollment, HealthProgram


class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name']


class EnrollmentSerializer(serializers.ModelSerializer):
    program = HealthProgramSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['program', 'date_enrolled']


class ClientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    enrollments = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'email', 'phone', 'enrollments']

    def get_full_name(self, obj):
        """Combine first, middle, and last names into one string."""
        names = [obj.first_name, obj.middle_name, obj.last_name]
        return " ".join(name for name in names if name)

    def get_enrollments(self, obj):
        """Return all programs the client is enrolled in."""
        enrollments = Enrollment.objects.filter(client=obj)
        return EnrollmentSerializer(enrollments, many=True).data

