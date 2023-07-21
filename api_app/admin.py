from django.contrib import admin

from api_app.models import CartItem
# Register your models here.

admin.site.register(CartItem)


"""We will use a serializer to convert our model object to JSON before we send the response.
 And when we receive a JSON request,
 our serializer will convert it to the model object, CartItem in this case.
 
 create a serializers.py file in the api_app folder and write a ModelSerializer for our model"""