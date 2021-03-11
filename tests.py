import os
import unittest

from config import basedir
from app import app, db
from app.models import User, Team

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/startseite', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_edituser(self):
        u1 = User(id=1, username='Testuser1', email='testmail1@tmail.com', teamid=1)
        u2 = User(id=2, username='Testuser2', email='testmail2@tmail.com', teamid=2)

        db.session.add(u1)
        db.session.add(u2)

        t1 = Team(id=1, bez='testteam1')
        t2 = Team(id=2, bez='testteam2')

        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

    def test_benutzeransicht(self):
        u1 = User(id=1, username='Testuser1', email='testmail1@tmail.com', teamid=1)
        u2 = User(id=2, username='Testuser2', email='testmail2@tmail.com', teamid=2)

        db.session.add(u1)
        db.session.add(u2)

        t1 = Team(id=1, bez='testteam1')
        t2 = Team(id=2, bez='testteam2')

        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        response = self.app.get('/benutzeransicht', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_deleteuser(self):
        u1 = User(id=1, username='Testuser1', email='testmail1@tmail.com', teamid=1)

        db.session.add(u1)

        t1 = Team(id=1, bez='testteam1')

        db.session.add(t1)
        db.session.commit()

        if not User.query.filter_by(id = id):
            pass


if __name__ == '__main__':
    unittest.main()