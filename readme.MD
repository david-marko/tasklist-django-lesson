# Todo List
- Get an Input
- Add or append it to an array.

# What a todo or task list is
- Title (Go to the cinema)
- Description (Go watch the new Superman movie)
- Due Date
- Priority (Low, Medium, High)
- Status (Done, Not Done) [ ]


task = {
    "id": 1
    "title": "",
    "description": "",
    "duedate": "",
    "priority": "",
    "status" : ""
}

all_tasks.append()


# Immigrations

- / - Gate
- /passports
- /national_ids
- /birth_certificates


- /passports
- /passports/apply
- /passports/renew/<str:passport_no>
- /passports/status/<str:passport_form>
- /passports/pay/<str:passport_form>

# Hospital Management
- / - Home page
- /doctors
- /patients
- /finance
- /pharmacy

- /doctors
- /doctors/login

- /patients/
- /patients/login
- /patients/appointments
- /patients/appointments/add
- /patients/appointments/<str:appointment_id>
- /patients/history
- /patients/prescription
- /patients/prescription/pay/<str:medication_id>

- /finance
- /finance/login 
(Get username and password, check if they are correct, if they are correct, then redirect the user to the transactions page, if they are wrong, tell them the username and password combination are incorrect)
if username == '' and password == '':
    then do this
else:
    do that
- /finance/transactions
- /finance/transactions/<int:transaction_id>
- /finance/add
Get the product, quantity and unit price
calculate the total
deduct a tax
register if its from cash, mobile money or bank transfer
register the transactions ID number
generate a reciept and redirect to the transactions page
total = unit_price * quantity
tax = 8/100
final_amount = total + (total * tax)

- /finance/search

# Dynamic URL Types
- str
- int
- slug (String)
- dates , YYYY, MM, DD
- regex (Regular Expressions) - /finance/search/<>


check if its a POST method
get the formdata from the HTML inputs
create an excerpt by getting the body and stripping away the characters leaving only the first 200 characters
create a new_post object
add it to the blog
redirect back to the blog page





# Models Datatypes
## String Related
- CharField
- TextField
- EmailField (I want a string, but as an email address)
- URLField (https://refactory.academy)

## Numeric Fields
- IntergerField 
- SmallIntegerField, BigIntegerField, PositiveIntegerField - Integers but of various sizes
- FloatField and DecimalField 0.23, 32.12

## Date and Time Fields
- DateField 15/07/2025
- DatetimeField 15/07/2025 10:05:43
- TimeField 10:05:43

## Boolean Field
- BooleanField (True or False)

## Files and Image Fields
- FileField
- ImageField

## Relationship Fields
- ForeignKey
- Manytomanyfield
- onetoonefield

- AutoField
- UUIDField
- BinaryField
