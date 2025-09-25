print('-'*10,'WELCOME TO VEGETABLE MARKET','-'*10)
print('tomato')
print('potato')
print('brinjal')
print('onion')
print('carrot')
print('beetroot')
print('chilli')
print('-'*10,'INVENTORY DETAILS','-'*10)

veg = ['brinjal','tomato','onion','potato','carrot','beetroot']
quantity=[40,30,50,20,10,30]
price=[10,20,40,30,20,10,]
sellingprice=[15,25,42,35,30,15]
user = {}

cart=[]
amount_list=[]
qty_list=[]
while True:

    print('1.Admin')
    print('2.User')
    print('3.Exit')
    role=int(input("Enter one option: "))
    if role == 1:
        print(''*10,'ADMIN BLOCK',''*10)
        id = 'Rupasri'
        passkey='rupa@123'
        userid =input("Enter a user id: ")
        password= input("Enter ur password: ")
        if userid==id and password==passkey:
            print('ok ur enter the correct password and user id')
            print('now ur the Admin')
            while True:
                print('-'*5,'choices','-'*5)
                print('1.Add item ')
                print('2.Remove item')
                print('3.Update item')
                print('4.View inventoroies')
                print('5 View user details')
                print('6.Report')
                print('7.Total revenue')
                print('8.Exit')
                    
                choose = int(input("Enter one option: "))
                if choose==1:
                    item =input (" enter name of item do you want to add: ")
                    if item in veg:
                        print('the', item,'is alredy available')
                    else:
                        veg.append(item)
                        price.append(int(input('price: ')))
                        quantity.append(int(input('Quantity: ')))
                        sellingprice.append(int(input('selling price: ')))
                        print ("item is added ")
                                                    
                elif choose==2:
                    item =input ("enter name of item do you want to remove: ")
                    if item in veg:
                        idx=veg.index(item)
                        veg.pop(idx)
                        quantity.pop(idx)
                        price.pop(idx)
                        sellingprice.pop(idx)
                        print('item is removed from veg')
                    else:
                        print(item,'is not found')
                            

                elif  choose==3:
                    item=input("Enter which item do you want to update: ")
                    if item in veg:
                        idx=veg.index(item)
                        price[idx] = int(input('new price: '))
                        quantity[idx] =int(input('new qty: '))
                        sellingprice[idx]=int(input('sp: '))
                        print('item is updated in inventory ')

                            
                elif  choose==4:
                    print('-'*50)
                    print(f"{'vegitale name':^15}{'availabel quantity':^15}{'buy price':^10}{'sale price':^10}")
                    print('-'*50)
                    for i in zip( veg,quantity,price,sellingprice):
                            print(f"{i[0]:^15}{i[1]:^15}{i[2]:^10}{i[3]:^10}")
                    print('-'*50)
                elif choose==5:
                    if user:
                        print("\n Registered users: ")
                        for name, number in user.items():
                            print(f"user:{name}, phone: {number}")

                    else:
                        print("no user registered yet")


                elif choose==6:
                   print(f"{'vegitale name':^15}{'sale':^15}{'profit':^10}")
                   total_revenue = 0
                   initial_quantity = [40, 30, 50, 20, 10, 30]
                   for i in range(len(veg)):
                        sold_qty=initial_quantity[i]-quantity[i]
                        profit = (sellingprice[i] - price[i]) * sold_qty
                        total_revenue =total_revenue+profit
                        for i in zip(veg,sold_qty,profit):
                            print(f"{i[0]:^15}{i[1]:^15}{i[2]:^10}")
                elif choose==7:
                    print('-'*10,'revenue','-'*10)
                    print(f"\nTotal Revenue: ₹{total_revenue}")
                    
                        
                elif choose==8:
                    print('coming out of the admin block')
                    break

          
            
        else:
            print('you enter the wrong credentails pls enter correctly')
            
    elif role==2:
        print( '-'*10,'User block','-'*10)
        print(''*10,'VEGETABLES',''*10)
        print('tomato')
        print('beetroot')
        print('carrot')
        print('potato')
        print('brinjal')
        print('onion')
        print('chillies')
        print('drumstick')
        name = input("Enter user name: ")
        number = input("Enter user ph number: ")
        user[name] = number
        if len(number)==10:
            print('user details are collected choose your options')
        else:
            print('your number is incorrect')
            
        while True:
             print('-'*10,'user choices','-'*10)
             print('1.Add cart')
             print('2.Remove cart')
             print('3.Modift cart')
             print('4.View cart')
             print('5.Billing')
             print('6.Exit')
             choice=int(input("enter your choice: "))
             if choice==1:
                 item= input('Enter which item do you want: ')
                 if item in veg:
                     qty = float(input("Enter how much qty do you want: "))
                     idx=veg.index(item)
                     if qty <= quantity[idx]:
                         cart.append(item)
                         qty_list.append(qty)
                         amount=qty*sellingprice[idx]
                         amount_list.append(amount)
                         quantity[idx] -=qty
                         print(item,'is added to cart')
                     else:
                         print('requested quantity is not  available')
                         
                 else:
                     print("item is not available")

             elif choice==2:
                item=input('Enter which item do you want to remove: ')
                if item in cart:
                    idx=cart.index(item)
                    quantity[veg.index(item)] += qty_list[idx]
                    cart.pop(idx)
                    qty_list.pop(idx)
                    amount_list.pop(idx)
                    print('item is removed from cart')
                else:
                    print('item is not available in cart')
                    
                         
             elif choice == 3:
                 item=input('Enter which item do you want to modify: ')
                 if item in cart:
                     idx=cart.index(item)
                     old_qty = qty_list[idx]
                     quantity[veg.index(item)]  +=old_qty
                     new_qty=int(input('Enter new quantity:'))
                     if new_qty<=quantity[veg.index(item)]:
                         qty_list[idx]=new_qty
                         amount_list[idx] = new_qty*sellingprice[veg.index(item)]
                         quantity[veg.index(item)] -= new_qty
                         print('item is modified')

                     else:
                         print("not enough stock")

                 else:
                     print("item is not in cart")



             elif choice == 4:
                 if not cart:
                     print("cart is empty")
                 else:
                     print("\n-----your cart------")
                     for item,qty in zip(cart,qty_list):
                         print(f"{item} ---{qty} kg ")
                     print("--------------------\n")
             elif choice == 5:
                 
                 for item, qty, amt in zip(cart, qty_list, amount_list):
                     print(f"{item} -- {qty} kg -- {amt} rupees")
                 print("\n---------------------------")    
                 total=sum(amount_list)
                 print(f"total bill amount: {total} rupees")
                 print("---------------------------\n")
                 
             elif choice==6:
                stop=input('do you want to exit(yes/no):')
                if stop == 'yes':
                    break


             else:
                print("invalid choice ,please try again")
    elif role == '3':
      print("exit")
      break
    
