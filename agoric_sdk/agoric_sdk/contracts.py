class Contract:
    def __init__(self, name):
        self.name = name
        self.terms = {}

    def set_terms(self, terms):
        self.terms = terms

    def get_terms(self):
        return self.terms
