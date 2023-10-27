from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking, Meal
from datetime import datetime


class IndexViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)


class MakeBookingViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.make_booking_url = reverse('booking')
        self.user = User.objects.create_user(
            'john', 'john@something.com', 'password')
        self.client.login(username='john', password='password')

    def test_make_booking(self):
        response = self.client.post(self.make_booking_url, {
            'date': '2023-10-26',
            'time': '14:00',
            'party_of': 3
        })
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Booking.objects.filter(
            date="2023-10-26", time="14:00").exists())

    def test_make_booking_existing_time(self):
        Booking.objects.create(
            date="2023-10-25", time="14:00", user=self.user, party_of=2)
        response = self.client.post(self.make_booking_url, {
            'date': '2023-10-25',
            'time': '14:00',
            'party_of': 4
        })
        self.assertEquals(response.status_code, 200)
        self.assertTrue(
            'A booking with this date and time already exists.' in response.content.decode())


class EditBookingViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.booking = Booking.objects.create(
            date="2023-10-25", time="14:00", user=self.user, party_of=2)
        self.client.login(username='testuser', password='testpassword')

    def test_edit_booking(self):
        
        response = self.client.post(reverse('edit_booking', args=[self.booking.id]), data={
            'date': '2023-10-26',
            'time': '15:00',
            'party_of': '4',
        })

        self.assertRedirects(response, reverse('booking'))


class CancelBookingViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'john@example.com', 'johnpassword')
        self.booking = Booking.objects.create(
            date="2023-10-25", time="14:00", user=self.user, party_of=2)
        self.client.login(username='john', password='johnpassword')

    def test_cancel_booking(self):
        response = self.client.post(
            reverse('cancel_booking', args=[self.booking.id]))
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())


class MealListViewTest(TestCase):

    def setUp(self):
        Meal.objects.create(title='Meal A', price=20.00)
        Meal.objects.create(title='Meal B', price=10.00)

    def test_meals_ordered_by_price(self):
        response = self.client.get(reverse('menu'))
        meals = list(response.context['meal_list'])
        self.assertEquals(meals[0].title, 'Meal B')
        self.assertEquals(meals[1].title, 'Meal A')
        self.assertEquals(meals[0].price, 10.00)
        self.assertEquals(meals[1].price, 20.00)
