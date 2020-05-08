
class EncodingMapper:

    def __init__(self):
        self.mapping = {'”': '"',
                        '–': '-',
                        '’': "'",
                        '“': '"'}
    def map(self, input_text: str) -> str:

        for key, value in self.mapping.items():
            input_text = input_text.replace(key, value)

        return input_text
