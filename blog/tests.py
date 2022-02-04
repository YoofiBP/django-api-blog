from django.test import TestCase
from .models import Post
from .models import User

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        testUser = User.objects.create(username='Yoofi')
        testUser.save()
        Post.objects.create(
            author=testUser, title='First Post', body='First Post Body').save()

    def test_post_model(self):
        post = Post.objects.get(id=1)
        postAuthor = f'{post.author}'
        postTitle = f'{post.title}'
        postBody = f'{post.body}'
        self.assertEqual(postAuthor, 'Yoofi')
        self.assertEqual(postTitle, 'First Post')
        self.assertEqual(postBody, 'First Post Body')
