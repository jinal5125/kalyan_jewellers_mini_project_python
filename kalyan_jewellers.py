name=input("Enter Your Name:")
gender=input("Enter Your Gender:")
age=int(input("Enter Your Age:"))
product=(input("Enter product:"))
gram=int(input("Enter product gram:"))

print("current gold price (1 gram) : 11633")
print("-------------------------")

gold_price = 11633


total = gold_price * gram
print(f"Total gold rate:{total}")


making_charge =845 * gram
print(f"making charge is:{making_charge}")
print("--------------------------")

total_amount = total + making_charge
print(f"total amount is:{total_amount}")
print("----------------------------")


if gender == "m":
    if age >= 65:
      if total_amount < 200000:
         print("No discount applicable")
         print(f"Net price is: {total_amount}")
      elif total_amount >= 200000 and total_amount <= 300000:
         discount=total_amount*20/100
         result=total_amount-discount
         print(f"Total discount amount is:{discount}")
         print("-----------------------------")
         print(f"Net price is:{result}")
      elif total_amount >= 300000 and total_amount <= 500000:
         discount=total_amount*30/100
         result=total_amount-discount
         print(f"Total discount amount is:{discount}")
         print("-----------------------------")
         print(f"Net price is:{result}")
      elif total_amount > 500000:
         discount=total_amount*35/100
         result=total_amount-discount
         print(f"Total discount amount is:{discount}")
         print("-----------------------------")
         print(f"Net price is:{result}")
    else:
       if total_amount < 200000:
         print("No discount applicable")
         print(f"Net price is: {total_amount}")
       elif total_amount >=200000 and total_amount <= 300000:
          discount=total_amount*10/100
          result=total_amount-discount
          print(f"Total discount amount is:{discount}")
          print("-----------------------------")
          print(f"Net price is:{result}")
       elif total_amount >= 300000 and total_amount <= 500000:
          discount=total_amount*20/100
          result=total_amount-discount
          print(f"Total discount amount is:{discount}")
          print("-----------------------------")
          print(f"Net price is:{result}")
       elif total_amount > 500000:
          discount=total_amount*25/100
          result=total_amount-discount
          print(f"Total discount amount is:{discount}")
          print("-----------------------------")
          print(f"Net price is:{result}")

elif gender =="f":
   if age >= 65:
      if total_amount < 200000:
         print("No discount applicable")
         print(f"Net price is: {total_amount}")
         print("-----------------------------")
      elif total_amount >= 200000 and total_amount <= 300000:
         print("Discount is 20%")
         discount=total_amount*20/100
         result=total_amount-discount
         print(f"Total discount amount is:{discount}")
         print("-----------------------------")
         print(f"Net price is:{result}")
      elif total_amount >= 300000 and total_amount <= 500000:
         print("Discount is 30%")
         discount=total_amount*30/100
         result=total_amount-discount
         print(f"Total discount amount is:{discount}")
         print("-----------------------------")
         print(f"Net price is:{result}")
      elif total_amount > 500000:
         print("Discount is 35%")
         discount=total_amount*35/100
         result=total_amount-discount
         print(f"Total discount amount is:{discount}")
         print("-----------------------------")
         print(f"Net price is:{result}")
   else:
       if total_amount < 200000:
         print("No discount applicable")
         print(f"Net price is: {total_amount}")
       elif total_amount >=200000 and total_amount <= 300000:
          print("Discount is 10%")
          discount=total_amount*10/100
          result=total_amount-discount
          print(f"Total discount amount is:{discount}")
          print("-----------------------------")
          print(f"Net price is:{result}")
       elif total_amount >= 300000 and total_amount <= 500000:
          print("Discount is 20%")
          discount=total_amount*20/100
          result=total_amount-discount
          print(f"Total discount amount is:{discount}")
          print("-----------------------------")
          print(f"Net price is:{result}")
       elif total_amount > 500000:
          print("Discount is 25%")
          discount=total_amount*25/100
          result=total_amount-discount
          print(f"Total discount amount is:{discount}")
          print("-----------------------------")
          print(f"Net price is:{result}")
else:
   print("invalid input")
