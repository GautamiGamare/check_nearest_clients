from django.db import models

class EmployeeModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode =models.IntegerField()
    state =models.CharField(max_length=50)

class Employee_location(models.Model):
    emp_id = models.OneToOneField(EmployeeModel,on_delete=models.CASCADE,primary_key=True)
    geocode = models.CharField(max_length=100,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


class CommonDistance(models.Model):
    emp_id = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE, primary_key=True)
    distance = models.FloatField()
    class Meta:
        abstract = True


class DistanceNewYork(CommonDistance):
    class Meta:
        verbose_name = "dist_new_york"

class DistanceBoston(CommonDistance):
    class Meta:
        verbose_name = "dist_boston"

class DistanceLosAngeles(CommonDistance):
    class Meta:
        verbose_name = "dist_los_angeles"

class DistanceChicago(CommonDistance):
    class Meta:
        verbose_name = "dist_chicago"

class DistanceHouston(CommonDistance):
    class Meta:
        verbose_name = "dist_houston"

class DistancePhoenix(CommonDistance):
    class Meta:
        verbose_name = "dist_phoenix"

class DistanceSanDiego(CommonDistance):
    class Meta:
        verbose_name = "dist_san_diego"

class DistanceDallas(CommonDistance):
    class Meta:
        verbose_name = "dist_dallas"

class DistanceSanJose(CommonDistance):
    class Meta:
        verbose_name = "dist_san_jose"

class DistanceAustin(CommonDistance):
    class Meta:
        verbose_name = "dist_austin"

class DistanceColumbus(CommonDistance):
    class Meta:
        verbose_name = "dist_columbus"


