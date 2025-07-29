#only printing the list of elements based on index
list=["hi","helloe","nani","hey"]
for i in list:
    print(i[1])
    print(i)
# first and last ones are ignored we take this type of code
for i in range(1,len(list)-1):

    print(list[i])

list=["grape", "mango","banana", "raw"]
for x in list:
     print(x)

#tuple also same for this 
tuple=(1,2,3,4,5,6)
for i in tuple:
    print(i)

#even length printing



ecommerce_data = [
    {
        "order_id": "ORD001",
        "customer_name": "Alice Johnson",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "quantity": 2,
        "price_per_unit": 599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD002",
        "customer_name": "Rajesh Kumar",
        "product": "Bluetooth Speaker",
        "category": "Electronics",
        "quantity": 1,
        "price_per_unit": 1999,
        "payment_method": "UPI",
        "delivery_status": "Shipped"
    },
    {
        "order_id": "ORD003",
        "customer_name": "Maria Fernandez",
        "product": "Leather Handbag",
        "category": "Fashion",
        "quantity": 1,
        "price_per_unit": 2499,
        "payment_method": "Cash on Delivery",
        "delivery_status": "Out for Delivery"
    },
    {
        "order_id": "ORD004",
        "customer_name": "John Smith",
        "product": "Running Shoes",
        "category": "Footwear",
        "quantity": 1,
        "price_per_unit": 3499,
        "payment_method": "Net Banking",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD005",
        "customer_name": "Anjali Mehta",
        "product": "Cotton Bedsheet Set",
        "category": "Home & Living",
        "quantity": 3,
        "price_per_unit": 899,
        "payment_method": "Credit Card",
        "delivery_status": "Cancelled"
    },
    {
        "order_id": "ORD006",
        "customer_name": "Samuel Lee",
        "product": "Smart Watch",
        "category": "Wearable Tech",
        "quantity": 1,
        "price_per_unit": 5299,
        "payment_method": "Debit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD007",
        "customer_name": "Neha Sharma",
        "product": "Makeup Kit",
        "category": "Beauty",
        "quantity": 2,
        "price_per_unit": 1499,
        "payment_method": "UPI",
        "delivery_status": "Processing"
    },
    {
        "order_id": "ORD008",
        "customer_name": "David Brown",
        "product": "Office Chair",
        "category": "Furniture",
        "quantity": 1,
        "price_per_unit": 4599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    }
]

for  x in ecommerce_data:
    if x["category"]=="Electronics":
      print(x)
print(ecommerce_data[-1]["product"])

#list index based printing even once only

list=["king","queen","assistance","employee","nani"]
for x in list:
    if len(x)%2==0:
        print(x)


dict={"name":"nani","age":24,"course":"mca"}
for i in dict:
    print(i)
    print(i,dict[i])

