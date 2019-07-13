class WrongDurationError(ValueError):
    def __str__(self):
        return 'Duration must be greater than 0'
