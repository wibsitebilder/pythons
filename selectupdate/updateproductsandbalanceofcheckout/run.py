import checkout
import qu
import products
import search
import sure
print("Hi")
products.newproduct = input("Please Inter a new product ")
products.newbalance = int(input("Please Inter the balance of the product "))
qu.newqua = int(input("Please inter the qua for the item "))
qu.quas[products.newproduct] = qu.newqua
products.products[products.newproduct] = products.newbalance
print("It's added sucsfully")
while True :
    search.search = input("What do you want (ni for new item , eib for edit the item balance , si for search the item balance , ck for new check out) , siq for search the item qua , eiq for edit item qua ) ")
    if search.search == "ni" :
        products.newproduct = input("Please Inter a new product ")
        products.newbalance = int(input("Please Inter the balance of the product "))
        qu.newqua = int(input("Please inter a new qua of the item "))
        products.products[products.newproduct] = products.newbalance
        qu.quas[products.newproduct] = qu.newqua
        print("It's added sucsfully")
    elif search.search == "eib" :
        search.searchitem = input("Please enter the item name ")
        search.searchbalance = int(input("Please enter a new balance of the item "))
        products.products[search.searchitem] = search.searchbalance
        print("It's edit sucsfully")
    elif search.search == "si" :
        search.searchitem = input("Please inter the item name ")
        search.itembalance = products.products.get(search.searchitem)
        print(f"The balance of the item is {search.itembalance}")
    elif search.search == "ck" :
        import checkout
        checkout.item1 = input("Please inter item 1 ")
        checkout.item1q = int(input("What's q "))
        import sure
        sure.item2sure = input("Do you have a item 2 ")
        if sure.item2sure == "yes" :
            checkout.item2 = input("Please inter item 2 ")
            checkout.item2q = int(input("What's q "))
            sure.item3sure = input("Do you have a item 3 ")
            if sure.item3sure == "yes" :
                checkout.item3 = input*("Please inter item 3 ")
                checkout.item3q = int(input("What's q "))
                sure.item4sure = input("Do you have a item 4 ")
                if sure.item4sure == "yes" :
                    checkout.item4 = input*("Please inter item 4 ")
                    checkout.item4q = int(input("What's q "))
                    sure.item5sure = input("Do you have a item 5 ")
                    if sure.item5sure == "yes" :
                        checkout.item5 = input*("Please inter item 5 ")
                        checkout.item5q = int(input("What's q "))
                        checkout.item1b = int(products.products.get(checkout.item1))
                        checkout.item2b = int(products.products.get(checkout.item2))
                        checkout.item3b = int(products.products.get(checkout.item3))
                        checkout.item4b = int(products.products.get(checkout.item4))
                        checkout.item5b = int(products.products.get(checkout.item5))
                        checkout.checkout = (checkout.item1b * checkout.item1q) + (checkout.item2b * checkout.item2q) + (checkout.item3b * checkout.item3q) + (checkout.item4b * checkout.item4q) + (checkout.item5b * checkout.item5q)
                        qu.quas[checkout.item1] = int(qu.quas.get(checkout.item1) - checkout.item1q)
                        qu.quas[checkout.item2] = int(qu.quas.get(checkout.item2) - checkout.item2q)
                        qu.quas[checkout.item3] = int(qu.quas.get(checkout.item3) - checkout.item3q)
                        qu.quas[checkout.item4] = int(qu.quas.get(checkout.item4) - checkout.item4q)
                        qu.quas[checkout.item5] = int(qu.quas.get(checkout.item5) - checkout.item5q)
                        print(f"The result is {checkout.checkout}")
                    else :
                        checkout.item1b = int(products.products.get(checkout.item1))
                        checkout.item2b = int(products.products.get(checkout.item2))
                        checkout.item3b = int(products.products.get(checkout.item3))
                        checkout.item4b = int(products.products.get(checkout.item4))
                        checkout.checkout = (checkout.item1b * checkout.item1q) + (checkout.item2b * checkout.item2q) + (checkout.item3b * checkout.item3q) + (checkout.item4b * checkout.item4q)
                        qu.quas[checkout.item1] = int(qu.quas.get(checkout.item1) - checkout.item1q)
                        qu.quas[checkout.item2] = int(qu.quas.get(checkout.item2) - checkout.item2q)
                        qu.quas[checkout.item3] = int(qu.quas.get(checkout.item3) - checkout.item3q)
                        qu.quas[checkout.item4] = int(qu.quas.get(checkout.item4) - checkout.item4q)
                        print(f"The result is {checkout.checkout}")
                else :
                    checkout.item1b = int(products.products.get(checkout.item1))
                    checkout.item2b = int(products.products.get(checkout.item2))
                    checkout.item3b = int(products.products.get(checkout.item3))
                    checkout.checkout = (checkout.item1b * checkout.item1q) + (checkout.item2b * checkout.item2q) + (checkout.item3b * checkout.item3q)
                    qu.quas[checkout.item1] = int(qu.quas.get(checkout.item1) - checkout.item1q)
                    qu.quas[checkout.item2] = int(qu.quas.get(checkout.item2) - checkout.item2q)
                    qu.quas[checkout.item3] = int(qu.quas.get(checkout.item3) - checkout.item3q)
                    print(f"The result is {checkout.checkout}")
            else :
                checkout.item1b = int(products.products.get(checkout.item1))
                checkout.item2b = int(products.products.get(checkout.item2))
                checkout.checkout = (checkout.item1b * checkout.item1q) + (checkout.item2b * checkout.item2q)
                qu.quas[checkout.item1] = int(qu.quas.get(checkout.item1) - checkout.item1q)
                qu.quas[checkout.item2] = int(qu.quas.get(checkout.item2) - checkout.item2q)
                print(f"The result is {checkout.checkout}")
        else :
            checkout.item1b = int(products.products.get(checkout.item1))
            checkout.checkout = int((checkout.item1b * checkout.item1q))
            qu.quas[checkout.item1] = int(qu.quas.get(checkout.item1) - checkout.item1q)
            print(f"The result is {checkout.checkout}")
    elif search.search == "siq" :
        search.searchitem = input("Please inter the item name ")
        qu.itemqua = qu.quas.get(search.searchitem)
        print(f"The qua of the item is {qu.itemqua}")
    elif search.search == "eiq" :
        search.searchitem = input("Please enter the item name ")
        qu.newquai = int(input("Please enter a new qua of the item "))
        qu.quas[search.searchitem] = qu.newquai
        print("It's edit sucsfully")