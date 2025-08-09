from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from menu.models import MealOption, Beverage
from blog.models import Post
from django.contrib.sites.models import Site
from django.utils import timezone

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

        # Create sample meal options if none exist
        if not MealOption.objects.exists():
            # Starters
            MealOption.objects.create(
                meal_name='Avocado Toast',
                description='Fresh avocado on sourdough bread with cherry tomatoes',
                price=8.99,
                meal_category=0,  # Starters
                available=True
            )
            
            # Mains
            MealOption.objects.create(
                meal_name='Quinoa Power Bowl',
                description='Quinoa with roasted vegetables and tahini dressing',
                price=12.99,
                meal_category=1,  # Mains
                available=True
            )
            MealOption.objects.create(
                meal_name='Vegan Burger',
                description='Plant-based burger with sweet potato fries',
                price=14.99,
                meal_category=1,  # Mains
                available=True
            )
            
            # Desserts
            MealOption.objects.create(
                meal_name='Chocolate Protein Ball',
                description='Raw cacao and almond protein balls',
                price=5.99,
                meal_category=2,  # Desserts
                available=True
            )
            
            self.stdout.write('Created sample meal options')

        # Create sample beverages if none exist
        if not Beverage.objects.exists():
            # Smoothie Blends
            Beverage.objects.create(
                beverage_name='Green Power Smoothie',
                description='Spinach, banana, apple, and protein powder',
                price=7.99,
                beverage_category=0,  # Smoothie Blends
                available=True
            )
            Beverage.objects.create(
                beverage_name='Berry Blast Smoothie',
                description='Mixed berries, yogurt, and honey',
                price=6.99,
                beverage_category=0,  # Smoothie Blends
                available=True
            )
            
            # Shake Varieties
            Beverage.objects.create(
                beverage_name='Chocolate Protein Shake',
                description='Rich chocolate with whey protein',
                price=8.99,
                beverage_category=1,  # Shake Varieties
                available=True
            )
            Beverage.objects.create(
                beverage_name='Vanilla Dream Shake',
                description='Vanilla ice cream with almond milk',
                price=7.99,
                beverage_category=1,  # Shake Varieties
                available=True
            )
            
            self.stdout.write('Created sample beverages')

        # Create sample blog post if none exist
        if not Post.objects.exists():
            admin_user = User.objects.get(username='admin')
            now = timezone.now()
            Post.objects.create(
                title='Welcome to Healthy Bites!',
                slug='welcome-to-healthy-bites',
                author=admin_user,
                created_date=now,
                updated_date=now,
                content='Welcome to our healthy eating blog. Discover nutritious recipes and wellness tips.',
                excerpt='Welcome to our healthy eating blog where we share nutritious recipes, wellness tips, and insights into maintaining a healthy lifestyle.',
                status=1  # Published
            )
            self.stdout.write('Created sample blog post')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))