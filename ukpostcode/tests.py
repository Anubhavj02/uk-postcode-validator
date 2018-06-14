import pytest # Pytest library for Python unit testing
from ukpostcode.postcode import Postcode


# List of all correct and valid UK post codes
formatting_positive_value = [
    "EC1A 1BB",  # already formatted
    "EC1A1BB",  # uppercase but no space
    "ec1a1bb",  # lower case with no spaces
    # Other combinations with varied length string
    "w1a0ax",
    "m11ae",
    "b338th",
    "cr26xh",
    "dn551pt"
]

# List of invalid postcodes with wrong length
formatting_negative_value_length = [
    "EC1A1BBasasas",  # more than 8 characters
    "EC",  # less than 5 characters
]

# List of invalid postcodes with special characters
formatting_negative_value_special_char = [
    "ec1#bb",  # special symbols #
    "m1$1ae"  # special symbols $
]

# List of all invalid UK post codes
validate_negative_values = [
    'QC1A 1BB',  # Invalid: The letters QVX are not used in the first position
    'VC1A 1BB',  # Invalid: The letters QVX are not used in the first position
    'XC1A 1BB',  # Invalid: The letters QVX are not used in the first position
    'AI1A 1BB',  # Invalid: The letters IJZ are not used in the second position
    'AJ1A 1BB',  # Invalid: The letters IJZ are not used in the second position
    'A9X 0AX',  # Invalid: only letters to appear in the third position are ABCDEFGHJKPSTUW
    'AA9C 0AX',  # Invalid: only letters to appear in the fourth position are ABEHMNPRVWXY
    'AA9A 9CZ',  # Invalid: inward code do not use CIKMOV
    'BBB 1AA',  # Invalid: all letters in outward code
    '1111 1AA',  # Invalid: all digits in Outward code
    '99AA 1AA',  # Invalid: all Digits post code area
    'AA1 AA',  # Invalid: all letters in inward code
]


@pytest.fixture(params=formatting_positive_value)
def formatting_positive_value(request):
    return request.param


@pytest.fixture(params=formatting_negative_value_length)
def formatting_negative_value_length(request):
    return request.param


@pytest.fixture(params=formatting_negative_value_special_char)
def formatting_negative_value_special_char(request):
    return request.param


def test_positive_format_postcode1(formatting_positive_value):
    """Function to test format_postcode method for positive cases

        arguments:
        formatting_positive_value -- list of valid uk post codes
    """
    postcode = Postcode()
    print(postcode.format_postcode(formatting_positive_value))
    # Message is "Formatted" if formatting of post code is successful
    assert postcode.message == "Formatted"


def test_positive_format_postcode2():
    """Function to test format_postcode method for positive cases

            arguments:
            formatting_positive_value -- list of valid uk post codes
    """
    postcode = Postcode()
    print(postcode.format_postcode("w1a0ax"))
    assert postcode.message == "Formatted" and postcode.formatted_postcode == "W1A 0AX"


def test_negative_format_postcode1(formatting_negative_value_length):
    """Function to test format_postcode method for negative cases(invalid length)

            arguments:
            formatting_positive_value -- list of post codes with invalid length
    """
    postcode = Postcode()
    print(postcode.format_postcode(formatting_negative_value_length))
    assert postcode.valid == False and postcode.message == "ERROR: 5 to 8 characters only"


def test_negative_format_postcode2(formatting_negative_value_special_char):
    """Function to test format_postcode method for negative cases(Special chars)

            arguments:
            formatting_positive_value -- list of post codes with special char
    """
    postcode = Postcode()
    print(postcode.format_postcode(formatting_negative_value_special_char))
    assert postcode.valid == False and postcode.message == "ERROR: No special Characters allowed"


@pytest.fixture(params=validate_negative_values)
def validate_negative_values(request):
    return request.param


def test_positive_validate_postcode1(formatting_positive_value):
    """Function to test validate_postcode method for positive cases

            arguments:
            formatting_positive_value -- list of valid uk post codes
    """
    postcode = Postcode()
    postcode.validate_postcode(formatting_positive_value)
    assert postcode.valid == True and postcode.message == "VALID: the post code is valid"


def test_negative_validate_postcode1(validate_negative_values):
    """Function to test validate_postcode method for negative cases

            arguments:
            validate_negative_values -- invalid uk post codes
    """
    postcode = Postcode()
    postcode.validate_postcode(validate_negative_values)
    assert postcode.valid == False and postcode.message == "INVALID: the post code is invalid"


def test_positive_split_postcode1():
    """Function to test split_validate_postcode method for positive cases;
       negative cases are handled by the methods this function call
    """
    postcode = Postcode()
    postcode.split_validate_postcode("SW1W 0NY")
    # Valid is equal to true for valid uk post codes and they splitted into respective components
    assert postcode.valid == True and postcode.postcode_area == "SW" and postcode.postcode_district == "1W" and\
           postcode.postcode_sector == "0" and postcode.postcode_unit == "NY"


def test_positive_split_postcode2():
    """Function to test split_validate_postcode method for positive cases;
       negative cases are handled by the methods this function call
    """
    postcode = Postcode()
    postcode.split_validate_postcode("M1 1AE")
    # Valid is equal to true for valid uk post codes and they splitted into respective components
    assert postcode.valid == True and postcode.postcode_area == "M" and postcode.postcode_district == "1" and\
           postcode.postcode_sector == "1" and postcode.postcode_unit == "AE"
