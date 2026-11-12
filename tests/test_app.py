import unittest

from application import create_app
from application.extensions import db
from application.models import Todo


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.context = self.app.app_context()
        self.context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def test_home_page_is_available(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TODO Lists", response.data)

    def test_todo_can_be_created_and_completed(self):
        response = self.client.post(
            "/",
            data={"title": "Prepare CI pipeline"},
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        todo = Todo.query.filter_by(title="Prepare CI pipeline").one()
        self.assertFalse(todo.status)

        response = self.client.get(f"/{todo.id}/done", follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Todo.query.get(todo.id).status)


if __name__ == "__main__":
    unittest.main()
