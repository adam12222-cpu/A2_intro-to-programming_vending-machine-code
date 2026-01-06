#intro to coding a2 vending macine

def main():
    print("=" * 20)
    print("VENDING MACHINE")
    print("=" * 20)
    print()
    
    vm_items={
        "item no. 1": {"name": "Aquafina", "price":1, "stock":6},
        "item no. 2": {"name": "lay's", "price":5, "stock":6},
        "item no. 3": {"name": "Kitkat", "price":8, "stock":6},
        "item no. 4": {"name": "Pepsi", "price":3, "stock":6},
        "item no. 5": {"name": "hershey's", "price":6, "stock":6},
        "item no. 6": {"name": "Coolaid", "price":3, "stock":6},
        "item no. 7": {"name": "Mentos", "price":2, "stock":6}
        }
    
    print("\n"+"="*40)
    print("ITEMS ON STOCK")
    print("=" * 40)
    print("item no. | Item name       | Price | Stock")
    print("=" * 40)
    
    for item_no, item in vm_items.items():
        name=item["name"]
        price=item["price"]
        stock=item["stock"]
        print(f"  {item_no}  | {name:<13} | {price:>5} AED | {stock:>2}")
        
    print()
        
    money_inserted=0
        
    print("=" * 40)
    print("Insert Money")
    print("=" * 40)
    print("the machine only accepts; 5, 10, 20, 50 AED notes")
    print("type the word 'done' if finished inserting cash")
    print()
        
    while True:
        money_input=input("enter cash:")
            
        if money_input.lower() == 'done':
                if money_inserted > 0:
                    break
                else:
                    print("you need to enter money first")
                    continue
            
        if money_input not in ['5', '10', '20', '50']:
                print("invalid amount, please only enter the valid choices")
                print("the machine only accepts; 5, 10, 20, 50 AED notes")
                continue
            
        money=int(money_input)
        money_inserted += money
        print(f"added {money} AED. total: {money_inserted}")
            
            
    print(f"\nyour total balance: {money_inserted} AED")
            
        
    print("=" * 40)
    print("select item")
    print("=" * 40)
            
   
    print("=" * 40)
            
    for item_no, item in vm_items.items():
        name=item['name']
        price=item['price']
        stock=item['stock']
        print(f"  {item_no}  | {name:<13} | {price:>5} AED | {stock:>2}")
                
    print()
            
    while True:
        item_choice=input("enter item no.:")
                
        if item_choice not in vm_items:
            print("invalid item, please choose on what's shown:")
            continue
                
        selected_item = vm_items[item_choice]
                
        if selected_item["stock"] <= 0:
            print(f"sorry, {selected_item['name']} is out of stock")
            continue
                
        if money_inserted < selected_item['price']:
            print(f"you dont have enough money to buy that... you need {selected_item['price'] - money_inserted} AED or more.")
            print("you can:")
            print("1. choose a cheaper item")
            print("2. cancel the purchace and refund cash")
                    
            choices=input("enter 1 or 2: ")
                    
            if choices == "2":
                print(f"\n transaction cancelled, returning {money_inserted} AED...")
                money_inserted = 0
                break
                    
            else: 
                continue
                    
        money_inserted -= selected_item['price']
        selected_item["stock"]-= 1
            
        print(f"\n"+"="*40)
        print("thank you for purchasing, come again")
        print("=" * 40)
        print(f"you bought: {selected_item['name']}")
        print(f"price: {selected_item['price']} AED")
    
        if money_inserted>0:
           print(f"change returned; {money_inserted} AED")
                         
        break
                        
if __name__=="__main__":
    main()
            
            
            
            
            
            
            
            
            
            
            