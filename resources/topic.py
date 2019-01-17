from flask_restful import Resource
from models.topic import TopicModel


class Topic(Resource):
    def get(self, topic):
        topic = TopicModel.find_by_topic(topic)
        if topic:
            return topic.json()
        return {'message': 'Topic not found.'}, 404

    def post(self, topic):
        if TopicModel.find_by_topic(topic):
            return {'message': "A topic '{}' already exists.".format(topic)}, 400

        topic = TopicModel(topic)
        try:
            topic.save_to_db()
        except:
            return {"message": "An error occured creating the topic."}, 500

        return topic.json(), 201

    def delete(self, topic):
        topic = TopicModel.find_by_topic(topic)
        if topic:
            topic.delete_from_db()

        return {'message': 'Topic deleted.'}

class TopicList(Resource):
    def get(self):
        return {'topic': list(map(lambda x:x.json(), TopicModel.query.all()))}