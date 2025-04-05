from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Seed permissions into the database'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Permission)

        # Define the permissions you want to create
        # Sau đó Chạy lệnh này để tạo seed nhé ae: python manage.py seed_permissions

        permissions = [
            {'codename': 'can_add_music', 'name': 'Can add music'},
        ]

        for perm in permissions:
            permission, created = Permission.objects.get_or_create(
                codename=perm['codename'],
                content_type=content_type,
                defaults={'name': perm['name']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Permission '{perm['name']}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Permission '{perm['name']}' already exists."))
                
