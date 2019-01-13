class Reservation:
    def __init__(self, meetup_id, topic, status):
        self.meetup_id = meetup_id
        self.topic = topic
        self.status = status
        self.db={
            "meetup":self.meetup_id,
            "topic":self.topic
        }

    def meetup_status(self):
        self.db["status"] = self.status        
        return self.db