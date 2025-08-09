from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from menu.models import MenuItem
from blog.models import Post
from django.contrib.sites.models import Site

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
            self.stdout.write('Created superuser: admin')

        # Update site domain
        site = Site.objects.get(pk=1)
        site.domain = 'healthy-bites-10.onrender.com'
        site.name = 'Healthy Bites'
        site.save()

        # Create sample menu items if none exist
        if not MenuItem.objects.exists():
            # Smoothies
            MenuItem.objects.create(
                name='Green Power Smoothie',
                description='Spinach, banana, apple, and protein powder',
                price=7.99,
                category='smoothie',
                available=True
            )
            MenuItem.objects.create(
                name='Berry Blast Smoothie',
                description='Mixed berries, yogurt, and honey',
                price=6.99,
                category='smoothie',
                available=True
            )
            
            # Milkshakes
            MenuItem.objects.create(
                name='Chocolate Protein Shake',
                description='Rich chocolate with whey protein',
                price=8.99,
                category='milkshake',
                available=True
            )
            MenuItem.objects.create(
                name='Vanilla Dream Shake',
                description='Vanilla ice cream with almond milk',
                price=7.99,
                category='milkshake',
                available=True
            )
            
            # Food items
            MenuItem.objects.create(
                name='Quinoa Power Bowl',
                description='Quinoa with roasted vegetables and tahini',
                price=12.99,
                category='food',
                available=True
            )
            MenuItem.objects.create(
                name='Vegan Burger',
                description='Plant-based burger with sweet potato fries',
                price=14.99,
                category='food',
                available=True
            )
            
            self.stdout.write('Created sample menu items')

        # Create sample blog post if none exist
        if not Post.objects.exists():
            admin_user = User.objects.get(username='admin')
            Post.objects.create(
                title='Welcome to Healthy Bites!',
                slug='welcome-to-healthy-bites',
                author=admin_user,
                content='Welcome to our healthy eating blog. Discover nutritious recipes and wellness tips.',
                status=1  # Published
            )
            self.stdout.write('Created sample blog post')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))