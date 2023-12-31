from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, Meal
import datetime

# Test class to test Booking model


class BookingModelTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='john', password='pass12345')

        # Create a booking associated with the user
        Booking.objects.create(
            user=self.user,
            name="John Doe",
            email="johndoe@example.com",
            date=datetime.date.today(),
            time=datetime.time(13, 0),
            party_of=3
        )

    def test_booking_creation(self):
        # Retrieve the created booking
        booking = Booking.objects.get(name="John Doe")

        # Assert that the booking attributes match the expected values
        self.assertEqual(booking.email, "johndoe@example.com")
        self.assertEqual(booking.user.username, "john")
        self.assertEqual(booking.party_of, 3)
        self.assertFalse(booking.approved)  # Assert that 'approved' is False


# Test class to test Booking model


class MealModelTest(TestCase):
    def setUp(self):
        # Create a meal
        Meal.objects.create(
            title="Vegan Pizza",
            description="Delicious vegan pizza with plant-based cheese and toppings.",
            excerpt="Best Vegan Pizza",
            price=12.00,
            food_type="vegan",
            meal_type="main"
        )

    def test_meal_creation(self):
        # Retrieve the created meal
        meal = Meal.objects.get(title="Vegan Pizza")

        # Assert that the meal attributes match the expected values
        self.assertEqual(
            meal.description, "Delicious vegan pizza with plant-based cheese and toppings.")
        self.assertEqual(meal.food_type, "vegan")
        self.assertEqual(meal.meal_type, "main")
