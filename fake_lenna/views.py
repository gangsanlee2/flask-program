from fake_lenna.models import LennaModel


class LennaController(object):
    model = LennaModel()

    def __init__(self):
        pass

    def __str__(self):
        return ""

    def preprocess(self, fname) -> object:
        model = self.model
        this = model.new_model(fname)
        return this

    def modeling(self, fname) -> object:
        this = self.preprocess(fname)
        return this

if __name__ == '__main__':
    pass