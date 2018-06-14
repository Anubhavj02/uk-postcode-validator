#! /usr/bin/env python3.6

import sys
from ukpostcode.postcode import Postcode


if __name__ == '__main__':

    # Get the input postcode string as the last parameter from the commandline
    postcode_str = sys.argv[-1]

    print("\nInput Post Code String: " + postcode_str)

    # Formatting the post code
    print("\n\n######### Formatting Postcode #########")
    postcode = Postcode()
    postcode.format_postcode(postcode_str)
    print("Message:", postcode.message)
    print("Formatted post code:", postcode.formatted_postcode)

    # Validating the post code
    print("\n\n######### Validating Postcode #########")
    postcode = Postcode()
    postcode.validate_postcode(postcode_str)
    print("Status:", postcode.valid)
    print("Message:", postcode.message)

    # Splitting the post code
    print("\n\n######### Formatting, Validating and Splitting Postcode #########")
    postcode = Postcode()
    postcode.split_validate_postcode(postcode_str)
    print("Status:", postcode.valid)
    print("Message:", postcode.message)
    print("Formatted post code:", postcode.formatted_postcode)
    print("Outward code:", postcode.outward_code)
    print("Inward code:", postcode.inward_code)
    print("postcode area:", postcode.postcode_area)
    print("postcode district:", postcode.postcode_district)
    print("postcode sector:", postcode.postcode_sector)
    print("postcode unit:", postcode.postcode_unit)
