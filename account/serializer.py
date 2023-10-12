from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):

       if data['first_name'] == "" or data['last_name'] == "":
         
         raise ValueError("input fields are required")
       
       else:
          return data
       
    
    def create(self, data):
       pwd = data['password']

       encrypted_pwd = make_password(pwd, "7y189eu2djweijcwouf9wiccjljd")
       
       user = User.objects.create(
          first_name = data['first_name'],
          last_name = data['last_name'],
          email = data['email'],
          photo = data['photo'],
          phone = data['phone'],
          username = data['username'],
          password = encrypted_pwd

       )
    
       return user
    


class LoginSerializer(serializers.Serializer):
   email = serializers.EmailField()
   password = serializers.CharField()
  

   def loginuser(self, data):
      user = User.objects.filter( email = data['email']).first()

      if user is not None:
         original_pwd = data['password']
         encrypted_pwd = getattr(user, "password")

         check = check_password(original_pwd, encrypted_pwd)

         if check == True:
            user = {
               "first_name": getattr(user, "first_name"),
               "last_name": getattr(user, "last_name"),
               "email": getattr(user, "email"),
               "id": getattr(user, "id")

            }
            return user

         else:
            
            raise ValueError("Invalid Credentials")
      
      else: 
         raise ValueError("Invalid Credentials")
      
   