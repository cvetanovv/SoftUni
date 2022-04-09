class Validator:
    @staticmethod
    def raise_if_string_is_empty(txt, error_message):
        if txt == "":
            raise ValueError(error_message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(number, error_message):
        if number <= 0:
            raise ValueError(error_message)