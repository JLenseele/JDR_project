class Dialogue:

    def __init__(self, id, content, next_id, description, end, quest=None):
        self.id = id
        self.content = content
        self.next = next_id
        self.descr = description
        self.end = end
        self.quest = quest

    def __str__(self):
        return self.content
