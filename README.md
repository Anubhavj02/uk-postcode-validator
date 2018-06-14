# UK Postcode Formatter, Validator and Splitter

A simple python library and django based application to demonstarte library usage for validating and formating UK post codes

![output](https://github.com/Anubhavj02/uk-postcode-validator/blob/master/output/output1.png)

## Requirements
* Pip 3
* virtualenv
* Python 3.6
* Pytest 3.6.1 (for unit test)
* Django 2.0.6 (only for django test application not required for library)

## Initial Setup
1. Create a virtual env
```shell
$ virtualenv -p python3 virtual_env_name
```
2. Activate the virtual environment
```shell
$ source virtual_env_name/bin/activate
```
3. Go the the cloned directory in command line
```shell
$ cd uk-postcode-validator
```
4. Add the requirements
```shell
$ pip3 install -r requirements.txt
```
5. To resolve any module import issues
```shell
$ export PYTHONPATH='.'
```

## UK Postcode Validator Library
1. On the command line; in the double quotes send the postcode you wish to validate
```shell
$ python ukpostcode "EC1A 1BB"
```
### Output:
![output](https://github.com/Anubhavj02/uk-postcode-validator/blob/master/output/output2.png)

2. As a library
```python
from ukpostcode.postcode import Postcode
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
```

3. Running Test cases
```shell
$ pytest ukpostcode/tests.py
```
![output](https://github.com/Anubhavj02/uk-postcode-validator/blob/master/output/output4.png)

## Testing the library using a Django App
### Setup
```shell
$ cd django_postcode
python manage.py runserver 0.0.0.0:8080
```
This will run the djaingo app on: http://127.0.0.1:8080/

### Output
Enter multiple postcode separated by semicolon in the box to validate, format and split
![output](https://github.com/Anubhavj02/uk-postcode-validator/blob/master/output/output3.png)
