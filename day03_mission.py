# 5.4,5.5

letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.'''.format(salutation = 'cool', name = 'munju', product = 'desk', verbed = 'was broken', room = 'studying room', animals = 'dogs', amount = 10, percent = 10)

print(letter)

