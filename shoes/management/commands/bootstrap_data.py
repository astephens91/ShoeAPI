from django.core.management.base import BaseCommand, CommandError
from shoes.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = "Populates ShoeColor and ShoeType data"

    def handle(self, *args, **options):
        ShoeColor.objects.create(color="Red")
        ShoeColor.objects.create(color="Orange")
        ShoeColor.objects.create(color="Yellow")
        ShoeColor.objects.create(color="Green")
        ShoeColor.objects.create(color="Blue")
        ShoeColor.objects.create(color="Indigo")
        ShoeColor.objects.create(color="Violet")
        ShoeColor.objects.create(color="White")
        ShoeColor.objects.create(color="Black")
        ShoeType.objects.create(style="Sneaker")
        ShoeType.objects.create(style="Boot")
        ShoeType.objects.create(style="Sandal")
        ShoeType.objects.create(style="Dress")
        ShoeType.objects.create(style="Other")