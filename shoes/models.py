from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=25)
    url = models.URLField(max_length=40)

    def __str__(self):
        return "{} @ {}".format(self.name, self.url)


class ShoeType(models.Model):
    STYLE_CHOICES = (
        ('SNEAKER', 'Sneaker'),
        ('BOOT', 'Boot'),
        ('SANDAL', 'Sandal'),
        ('DRESS', 'Dress'),
        ('OTHER', 'Other')
    )

    style = models.CharField(max_length=25)

    def __str__(self):
        return "{}".format(self.style)


class ShoeColor(models.Model):
    COLOR_CHOICES = (
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('YELLOW', 'Yellow'),
        ('GREEN', 'Green'),
        ('BLUE', 'Blue'),
        ('INDIGO', 'Indigo'),
        ('VIOLET', 'Violet'),
        ('WWHITE', 'White'),
        ('BLACK', 'Black')
    )
    color = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.color)


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=25)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=25)

    def __str__(self):
        return "{} by {}".format(self.brand_name, self.manufacturer)
        
