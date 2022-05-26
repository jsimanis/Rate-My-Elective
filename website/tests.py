from django.test import TestCase
from django.contrib.auth import get_user_model
from website.models import Course, Contact, Department, Review
from website.forms import ContactForm, AddClassForm, ReviewForm
from django.urls import reverse
from http import HTTPStatus

User = get_user_model()


class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='correctUsername', password='correctPass', email='test@test.com')

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post('login/', {
            'username': 'correctUsername',
            'password': 'correctPass'
        })
        self.assertTrue(response.data['authenticated'])

    def test_wrong_username(self):
        response = self.client.post('login/', {
            'username': 'wrongUsername',
            'password': 'correctPass'
        })
        self.assertFalse(response.data['authenticated'])

    def test_wrong_password(self):
        response = self.client.post('login/', {
            'username': 'correctUsername',
            'password': 'wrongPass'
        })
        self.assertFalse(response.data['authenticated'])

class RegisterTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password'

    def test_register_url(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_register_form(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)



class AddReviewTest(TestCase):
  def setup(self):
    self.user = User.objects.create_user(
    username='correctUsername', password='correctPass', email='test@test.com')
    self.department = Department.objects.createDepartment(
      code="IT",
      name="Information Technology"
    )
    self.elective = Course.objects.creatCourse(
      name= 'Software Engineering',
      course_number=326,
      department=self.department,
      description="description",
      flagged=False 
    )
    self.review= Review.objects.createReview(
      content="content",
      rating_positive=1,
      rating_negative=0,
      year_taken=2021,
      author=self.user,
      course=self.elective,
      flagged=False
    )

  def add_review(self):
    form = ReviewForm(data={"content":"content",
      "rating_positive":1,
      "rating_negative":0,
      "year_taken":2021,
      "author":self.user,
      "course":self.elective,
      "flagged":False}
    )

    self.assertEqual(form.content, "content")


  def get_review(self):
    response = self.client.get('/elective/IT/326')
    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertEqual(response.content, self.review.content)

class ContactAdminTest(TestCase):
  def setUp(self):
    pass

  def test(self):
    self.contactobj = Contact.objects.createContact(name = "Joe shmo", email = "hello@gmail.com", query = "website crashed")
    self.assertTrue(isinstance(self.contactobj, Contact))

  def tearDown(self):
      self.contact.delete()

class AddClassTest(TestCase):
  def setUp(self):
    self.dept = Department.objects.createDepartment(code = "HIS", name = "History")

  def test(self):
    self.course_obj = Course.objects.createCourse(department= self.dept, course_number = "234", name = "World History", description = "Intro to World History")
    self.assertTrue(isinstance(self.course_obj, Course))

  def tearDown(self):
      self.dept.delete()
      self.course.delete()

class RemoveClassTest(TestCase):
  def setUp(self):
    self.dept = Department.objects.createDepartment(code = "HIS", name = "History")
    self.course_obj = Course.objects.createCourse(department= self.dept, course_number = "234", name = "World History", description = "Intro to World History")

  def test(self):
    Course.objects.delete(self.course_obj)
    self.assertFalse(isinstance(self.course_obj, Course))

  def tearDown(self):
      self.dept.delete()
      self.course.delete()