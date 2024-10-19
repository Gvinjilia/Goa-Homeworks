#გამოიტანეთ თქვენი სახელი და გვარი იმდენჯერ, რამდენი წლისაც ხართ
for name in range(13):
    print("nino")

#გამოიტანეთ ტერმინალში რიცხვები 1-დან 20-ის ჩათვლით
for i in range(21):
    print(i)

#გამოიტანეთ ტერმინალში რიცხვები 20-დან 0-მდე
for i in range(21,0,-1):
    print(i)

#დაბეჭდეთ 1-დან 5-ის ჩათვლით რიცხვთა კვადრატი(n * n)
for i in range(5):
    print(i*i)

#დაბეჭდეთ ყველა ლუწი რიცხვის ჯამი 1-დან 10-ის ჩათვლით
for i in range(11):
    print(i+i)

#მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ცვლადში, შემდეგ კი 0-დან 
#შემოტანილი რიცხვის ჩათვლით შეამოწმეთ, თუ ლუწია დაბეჭდეთ რიცხვი is Even, სხვა 
#შემთხვევაში რიცხვი is Odd;(მაგალითად 4, ლუწია ამიტომაც დაბეჭდავთ "4 is Even")
num=(input("enter the number:"))
if num=="1":
    print("1 is odd")
elif num=="3":
     print("3 is odd")
elif num=="5":
     print("5 is odd")
elif num=="7":
     print("7 is odd")
elif num=="9":
     print("9 is odd")

if  num=="2":
    print("4 is even")
elif num=="4":
     print("4 is even")
elif num=="6":
      print("6 is even")
elif num=="8":
      print("8 is even")
elif num=="10":
     print("10 is even")





