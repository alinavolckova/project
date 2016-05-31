class SearcherException(Exception):

    message = ""

    def __init__(self, p_message):
        self.message = p_message

    def __str__(self):
        return self.message