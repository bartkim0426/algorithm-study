delivery_fee = 2500
discount = 6000
price = 4700
min_delivery = 30000

total_discount = 100000
for i in range(1,10):
    total = price * i
    if total > min_delivery:
        discount = (total - discount)//i
    else:
        discount = (total - discount + delivery_fee)//i
    print(i)
    print(discount)
    print((100000//6000) * i)
