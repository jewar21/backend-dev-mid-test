from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, TIMESTAMP, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Muchos a muchos entre Post y Tag
post_tags = Table(
    'post_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    posts = relationship('Post', secondary=post_tags, back_populates='tags')