class ImageFileAcceptor:

    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file):
        return file.split(".")[-1] in self.extensions
