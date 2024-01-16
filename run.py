#!/usr/bin/python3
"""Flask application."""
from flaskblog import app, db
from flaskblog.models import User, Post


with app.app_context():
    db.drop_all()
    db.create_all()
    user_1 = User(username='Corey', email='c@demo.com', password='password')
    user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
    db.session.add_all([user_1, user_2])
    db.session.commit()
    
    users = db.session.execute(db.select(User)).scalars().first()
    print(users.id)
    post_1 = Post(title='Post 1', content='Content is first post', user_id=users.id)
    db.session.add(post_1)
    db.session.commit()
    print(users.posts)
    post = db.session.execute(db.select(Post)).scalars().first()
    print(post.author)
    # db.drop_all()

    


if __name__ == '__main__':
    app.run(debug=True)