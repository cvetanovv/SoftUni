class Validator:
    @staticmethod
    def raise_if_string_is_null_or_empty(txt, error_message):
        if txt.strip() == "":
            raise ValueError(error_message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(number, error_message):
        if number <= 0:
            raise ValueError(error_message)

    @staticmethod
    def raise_if_number_out_of_range(number, min_value, max_value, error_message):
        if number < min_value or number > max_value:
            raise ValueError(error_message)