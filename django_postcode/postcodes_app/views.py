from django.http import HttpResponse
from django.shortcuts import render
from ukpostcode.postcode import Postcode


def index(request):
    """function to display the starting point of the application"""
    return render(request, 'validate_postcode.html')


def check(request):
    """function to perform formatting, validation and splitting of UK postcodes"""

    if request.method == 'POST':
        # Get the list of postcodes
        postcodes = request.POST.get('postcodes', '')
        # Split the postcpdes by semicolon
        postcode_list = postcodes.split(";")
        postcode_checked_list = []

        # iterate through all the input postcodes
        for postcode in postcode_list:
            postcode_obj = Postcode()
            # Check for validity and split
            postcode_obj.split_validate_postcode(postcode)
            # Add post code object list
            postcode_checked_list.append(postcode_obj)
        return render(request, 'validate_postcode.html', locals())

    return render(request, 'validate_postcode.html')


