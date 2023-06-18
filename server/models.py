from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 
    @validates('phone_number')
    def validate_phone_number(self, key ,phone_number):
        if len(str(phone_number)) == 10:
            return phone_number
        else:
            raise ValueError('Invalid phone number')
        
    @validates('name')
    def validate_name(self, key, name):
        if len(name) == 0:
            raise ValueError('Failed to validate name')
        else:
            return name
        

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 
    @validates('content')
    def validate_content(self, key, post_content ):
        if len(post_content) >= 250:
            return post_content
        else:
            raise ValueError('failed to validate content length')
        
    @validates('category')
    def validate_category(self, key, post_category ):
        if post_category in ['Fiction', 'Non-Fiction']:
            return post_category
        else:
            raise ValueError('failed to validate category type')
        
    @validates('summary')
    def validate_summary(self, key, post_summary):
        if len(post_summary ) >250:
            raise ValueError('failed to validate summary')
        else:
            return post_summary
        
    @validates('title')
    def validate_title(self, key, post_title):
        if "Won't Believe" and "Secret" and "Top" and "Guess" in post_title:
            return post_title
        else:
            raise ValueError('failed to validate title')


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
