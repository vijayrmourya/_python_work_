import credit_card_validator

print("welcome to credit card validator!")
credit_card_validator.details()
while 1:
    card_number = input("Enter your card number:\n")
    print(card_number + "->" + "valid card") if credit_card_validator.validate_card(card_number) else print(
        card_number + "->" + "Invalid card")
    another = input("Do you want to check another card (y/n):")
    if another == 'n':
        break
