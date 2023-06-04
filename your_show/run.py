import posts
import want
import oregnal
import yourshowresult
import accountsyourshow
accountsyourshow.newaccount = input("Please Enter a new account name ")
print("wait.....")
numbers2 = 0
numbersofnumber2 = int(numbers2 + 1)
numbers2 = numbersofnumber2
accountsyourshow.accounts = {numbers2 : accountsyourshow.newaccount}
print("it's added sucsusfully")
while True :
    want.want1 = input("What do you want please select ( ap of add post , spa of search post address , spn of search post number , aa of add account , san of search account number ) ? ")
    numbers = 0
    if want.want1 == "ap" :
        oregnal.address = input("What's address ? ")
        oregnal.text = input("What's text of the post or address ? ")
        want.want4 = input("Do you want a custom number please select ( y of yes , n of no ) ")
        if want.want4 == "y" :
            want.want5 = int(input("What's number "))
            print("wait.....")
            posts.posts = {oregnal.address : oregnal.text}
            posts.numberofposts = {want.want5 : oregnal.address}
            print("It's added sucsusfully")
        elif want.want4 == "n" :
            print("Wait.....")
            posts.posts = {oregnal.address : oregnal.text}
            numberofpost = int(numbers + 1)
            numbers = numberofpost
            posts.numberofposts = {numbers : oregnal.address}
            print("It's added sucsusfully")
        else :
            print("I'm sorry it's not supported now plese retry")
    elif want.want1 == "spa" :
        want.want2 = input("Please input address ")
        print("wait.....")
        yourshowresult.result1 = posts.posts.get(want.want2)
        print(f"This is text of the post is {yourshowresult.result1}")
    elif want.want1 == "spn" :
        want.want3 = int(input("Please inter number "))
        print("wait.....")
        yourshowresult.result2 = posts.numberofposts.get(want.want3)
        yourshowresult.result3 = posts.posts.get(yourshowresult.result2)
        print(f"The text of the address is {yourshowresult.result3}")
    elif want.want1 == "aa" :
        accountsyourshow.newaccount = input("please inter account name ")
        print("wait.....")
        numbers2 = 0
        numbersofnumber2 = numbers2 + 1
        numbers2 = numbersofnumber2
        accountsyourshow.accounts = {numbersofnumber2 : accountsyourshow.newaccount}
        print("it's added sucsusfully")
    elif want.want1 == "san" :
        want.want6 = int(input("Please inter account number "))
        print("wait.....")
        yourshowresult.result4 = accountsyourshow.accounts.get(want.want6)
        print(f"The account name is {yourshowresult.result4}")
    else :
        print("I'm sorry it's not supported now plese retry")