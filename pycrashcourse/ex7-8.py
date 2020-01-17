sandwich_orders = ["tuna", "peanut_butter", "ham & swiss", "grilled_cheese",]
finished_orders = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_orders.append(sandwich)

print("\n These orders have been finished.")
for order in finished_orders:
    print(order)