from db import db

class TopicModel(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80))

    articles = db.relationship('ArticleModel', lazy='dynamic')

    def __init__(self, topic):
        self.topic = topic
    
    def json(self):
        return {'topic': self.topic, 'articles': [article.json() for article in self.articles.all()]}
    
    @classmethod
    def find_by_topic(cls, topic):
        return cls.query.filter_by(topic=topic).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
