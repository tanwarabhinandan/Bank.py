print("Welcome to Citizen Bank")

bal = 1000
dep = 0

print("Please press 'b' for balance")
print("Please press 'd' for deposit")
print("Please press 'w' for withdraw")
print("Please press 'e' for exit")

while True:

	key_press = input(">> ")

	if key_press == "b":
		print(f"Your account balance = {bal}")
	elif key_press == "d":
		dep = int(input("Please enter amount to deposit: "))
		bal = bal + dep
		print(f"Your new balance is = {bal}")
	elif key_press == "w":
		dep = int(input("Please enter amount to withdraw: "))
		bal = bal - dep
		print(f"Your new balance is = {bal}")
	else:
		key_press == "e"
		print("Good bye...!!!")
		break