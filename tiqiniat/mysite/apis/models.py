from django.db import models
# Create your models here.
seperatetype={(1,'Array Of String'),(2,'comma')}
ratetype={(1,'stars'),(2,'numbers')}
priceTypeChoices={('1','Fare'),('2','Price')}
hotelsKeys=[(1,'hotal'),(2,'hotelname')]
class providers(models.Model):
    providerName=models.CharField(max_length=200)
    providerHotelKey=models.IntegerField(choices=hotelsKeys,null=True)
    seprately=models.IntegerField(choices=seperatetype)
    ratetype=models.IntegerField(choices=ratetype)
    HasDiscount=models.BooleanField(default=False)
    priceType=models.CharField(choices=priceTypeChoices,max_length=100)
    
    def __str__(self):
        return str(self.id)
class amenities(models.Model):
    amenityName=models.CharField(max_length=200)
    def __str__(self):
        return self.amenityName
class cities(models.Model):
    cityName=models.CharField(max_length=200)
    def __str__(self):
        return self.cityName
class hotels(models.Model):
    provider=models.ForeignKey(providers,related_name='hotels',on_delete=models.CASCADE)
    hotelName=models.CharField(max_length=200)
    rate=models.IntegerField()
    price=models.FloatField()
    amenities=models.ManyToManyField(amenities,related_name="amenities")
    city=models.ForeignKey(cities,related_name='hotelsCity',on_delete=models.CASCADE)
    def __str__(self):
        return "Hotel : {} city: {} uder provider {}".format(self.hotelName,self.city.cityName,self.provider.providerName)


