from db import db

class ArticleModel(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String())

    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    topic = db.relationship('TopicModel')

    def __init__(self, title, content, topic_id):
        self.title = title
        self.content = content
        self.topic_id = topic_id
        
    def json(self):
        return {'title': self.title, 'content': self.content}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
