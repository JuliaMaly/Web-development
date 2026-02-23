from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, video_title):
        pass


class User(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, video_title):
        print(f"{self.name} received notification about: {video_title}")


class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(video_title)

    def publish_video(self, video_title):
        print(f"{self.name} published new video: {video_title}")
        self.notify(video_title)


if __name__ == "__main__":
    channel = YouTubeChannel("Tech Channel")

    user1 = User("Alice")
    user2 = User("Bob")

    channel.subscribe(user1)
    channel.subscribe(user2)

    channel.publish_video("Design Patterns in Python")