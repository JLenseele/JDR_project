class Dialogue:

    def __init__(self, id, content, next_id, description, end):
        self.id = id
        self.content = content
        self.next = next_id
        self.descr = description
        self.end = end

    def __str__(self):
        return self.content


class Pnjdialogue(Dialogue):

    def __init__(self, id, content, next_id, description, end):
        super().__init__(id=id,
                         content=content,
                         next_id=next_id,
                         description=description,
                         end=end)
        self.next = []


class Playerdialogue(Dialogue):

    def __init__(self, id, content, next_id, description, end, accept_quest=None):
        super().__init__(id=id,
                         content=content,
                         next_id=next_id,
                         description=description,
                         end=end)
        self.accept_quest = accept_quest


