import re  # regular expression library in python


class Postcode(object):
    """ Class PostCode to represent various attributes and functionalities corresponding to uk post code like
        formatting, validating and splitting

        Attributes:
            input_postcode: input postcode to be checked and validated
            formatted_postcode: A string to contain the proper formatted version of the post code
            outward_code: A string to hold the first group of the post code(Postcode area and district- 2 to 4 chars)
            inward_code: A string to hold the second group of the post code(Postcode sector and unit- 3 chars)
            postcode_area: A string to area of post code(either one or two characters long and is all letters)
            postcode_district: A string to hold district(one or two digits (and sometimes a final letter))
            postcode_sector: A string to hold sector(first character of the inward code)
            postcode_unit: A string to hold unit(two characters added to the end of the postcode sector)
            valid: A boolean flag to state the validity of the postcode
            message: A string to state the status of the post code (valid or error message)

    """

    # Format Acceptable : AA9A 9AA | A9A 9AA | A9 9AA | A99 9AA | AA9 9AA | AA99 9AA
    # Regex expression to validate the postcode it has following conditions:
    # 1. letters QVX are not used in the first position
    # 2. letters IJZ are not used in the second position
    # 3. only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A
    # 4. only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A
    # 5. final two letters in inward code do not use the letters CIKMOV

    POSTCODE_REGEX = r"^(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW])" \
                     r" ?[0-9][ABD-HJLNP-UW-Z]{2})$"

    # compile the regex
    VALID_POSTCODE_REGEX = re.compile(POSTCODE_REGEX)

    # Special case and conditions

    # Areas with only single-digit districts: BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    SINGLE_DIGIT_POSTAREA = ['BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WC', 'WN', 'ZE']

    # Areas with only double-digit districts: AB, LL, SO
    DOUBLE_DIGIT_POSTAREA = ['AB', 'LL', 'SO']

    # Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS
    ZERO_DIGIT_POSTAREA = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS']

    # central London single-digit districts have been further divided by inserting a letter after the digit and before
    #  the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2
    LETTER_FOLLOW = ['EC1', 'EC2', 'EC3' 'EC4', 'SW1', 'W1', 'WC1', 'WC2']

    # Special valid outward codes:
    # 1. although WC is always subdivided by a further letter, e.g. WC1A
    # 2. BS is the only area to have both a district 0 and a district 10
    # 3. part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P)
    SPECIAL_COND_OUTWARD = ['WC1A', 'BS10', 'E1W', 'N1C', 'N1P', 'NW1W', 'SE1P']

    # Special invalid outward codes
    INVALID_OUTWARD = ['E1', 'N1', 'NW1', 'SE1', 'EC50']

    def __init__(self, input_postcode = "", formatted_postcode = "", outward_code="", inward_code="", postcode_area="", postcode_district="", postcode_sector="",
                 postcode_unit="", valid = False, message = ""):
        """Constructor to initialize the Postcode object with the default or supplied values"""
        self.input_postcode = input_postcode
        self.formatted_postcode = formatted_postcode
        self.outward_code = outward_code
        self.inward_code = inward_code
        self.postcode_area = postcode_area
        self.postcode_district = postcode_district
        self.postcode_sector = postcode_sector
        self.postcode_unit = postcode_unit
        self.valid = valid
        self.message = ""

    def format_postcode(self, postcode_str):
        self.input_postcode = postcode_str
        """Function to format the post code and return the formatted value with inward and outward code

                arguments:
                postcode_str -- input post code string
        """

        # Replace all the space from the string
        postcode_str = postcode_str.replace(" ", "")

        # Check the length of input postcode and return error message if len of postcode(with space) is greater than 7
        # chars and less than 5 chars
        if len(postcode_str) < 5 or len(postcode_str) > 7:
            self.message = "ERROR: 5 to 8 characters only"
            return self.message

        # Throw error message if the input postcode contains special symbols
        if not postcode_str.isalnum():
            self.message = "ERROR: No special Characters allowed"
            return self.message

        # Converting the post code to upper case
        postcode_str = postcode_str.upper()
        # Extracting out the outward code from input postcode string as all chars except last 3
        self.outward_code = postcode_str[:-3]
        # Extracting out the inward code as last 3 chars from input postcode string
        self.inward_code = postcode_str[-3:]
        # Joining the outward and inward code separated by space to form formatted postcode
        self.formatted_postcode = self.outward_code + " " + self.inward_code
        self.message = "Formatted"

        return self.formatted_postcode

    def validate_postcode(self, postcode_str):
        """Function to validate the input postcode string and return true if valid and else false for invalid postcode

                arguments:
                postcode_str -- input post code string
        """

        # First format the input postcode
        self.format_postcode(postcode_str)

        # If the formatting of postcode is successful
        if self.message == "Formatted":
            # Match the formatted postcode with the compliled regex, valid = true if matched else valid = false
            if self.VALID_POSTCODE_REGEX.match(self.formatted_postcode):
                self.valid = True
                self.message = "VALID: the post code is valid"
                return self.valid
            else:
                self.message = "INVALID: the post code is invalid"
                return self.valid

    def split_validate_postcode(self, postcode_str):
        """Function to validate, format and split the input post code into individual components

                arguments:
                postcode_str -- input post code string
        """
        if self.validate_postcode(postcode_str):

            # Split the outward code on first digit to get area and district
            # Example outward code: SW1W; area: SW and district: 1W

            # Index of first digit in outward code
            district_start = re.search("\d", self.outward_code).start()
            # if outward code contains a digit
            if district_start:
                # Get the area from the outward code as all the characters before the first digit in outward code
                self.postcode_area = self.outward_code[:district_start]
                # Get the district from the outward code as all the characters from the first digit in outward code
                self.postcode_district = self.outward_code[district_start:]

                # Checking special conditions
                if not (self.outward_code in self.SPECIAL_COND_OUTWARD):
                    if self.outward_code.startswith(tuple(self.LETTER_FOLLOW)):
                        if not self.postcode_district[-1:].isalpha():
                            self.message = "INVALID: the post code is invalid"
                            self.valid = False

                    elif self.postcode_area in self.DOUBLE_DIGIT_POSTAREA:
                        if len(self.postcode_district) != 2 or not (self.postcode_district.isdigit()):
                            self.message = "INVALID: the post code is invalid"
                            self.valid = False

                    elif self.postcode_area in self.ZERO_DIGIT_POSTAREA:
                        if self.postcode_district != '0':
                            self.message = "INVALID: the post code is invalid"
                            self.valid = False
                    elif self.postcode_area in self.SINGLE_DIGIT_POSTAREA:
                        if len(self.postcode_district) != 1 or not (self.postcode_district.isdigit()):
                            self.message = "INVALID: the post code is invalid"
                            self.valid = False

                    if self.outward_code.startswith(tuple(self.INVALID_OUTWARD)):
                        self.message = "INVALID: the post code is invalid"
                        self.valid = False

            if self.valid:
                # Split the inward code to get sector and unit
                # Example inward code: 0NY; sector: 0 and unit: NY

                # Get the sector from inward code as the first letter
                self.postcode_sector = self.inward_code[:1]
                # Get unit from inward code as last 2 letters
                self.postcode_unit = self.inward_code[1:]
            else:
                self.postcode_area = ""
                self.postcode_district = ""
