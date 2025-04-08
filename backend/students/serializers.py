from rest_framework import serializers
from .models import RegisterStudents

class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 🔥 Ensure password is not exposed in API response

    class Meta:
        model = RegisterStudents
        fields = ["StudentId", "FirstName", "SecondName", "PhoneNumber", "Email", "Country", "DateOfBirth", "Gender", "password"]
        read_only_fields = ["StudentId"]  # 🔥 StudentId is autogenerated, don't allow input

    def create(self, validated_data):
        """Create and hash password correctly"""
        # print(f"in serail {validated_data}")
        password = validated_data.pop("password")
        student = RegisterStudents(**validated_data)
        student.set_password(password)  # 🔥 Hash the password properly
        student.save()
        return student
    
