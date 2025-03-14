descriptionList = ["""
The system functional requirements are as follows:
1) Manage customer information, including customer ID.
2) Manage product information, including product name and description.
3) Manage order information, including order ID and order date.
4) Each customer can place multiple orders.  Each order can include multiple products. For each product in an order, the system stores important details including the quantity and price.
5) Manage customer reviews. Customers who have purchased a product can leave a review. Each review includes the review date and rating.
6) Manage promotions.  Each product can be part of multiple promotional campaigns. The system stores promotion details, including the discount rate, start date, and end date.
7) Calculate the order amount for each customer. The order amount = Σ (product quantity * product price). Note that the product within the validity period( between start date and end date) of a promotion should have the discounted price considered in the order amount calculation.
""",
#  Note that the product within the validity period of a promotion should have the discounted price considered in the order amount calculation.
#  Note that the product which is part of a promotion should have the discounted price considered in the order amount calculation. 

"""For an e-commerce platform customers identified with an ID place orders with multiple products. Each product has a name and description. The products included in the order have important details such as the quantity and price.

Additionally, the platform receives reviews from the customers who purchased the product. Products receives multiple reviews from customers and the review date and rating is tracked. 
                   The platform permits the management of promotions, where products can be part of various promotional campaigns. 
                   The system stores the details of promotions including discount rates and validity periods."""

]


umlList = ["""
```plantuml
@startuml
class Customer {
    - string ID
}

class Product {
    - string Name
    - string Description
}

class Order {
    - string ID
    - date Date

    + float calculateOrderAmount(Date)
}

class OrderDetails {
    - int Quantity
    - float Price
    
    + float calculateProductAmount(Date, product)
}

class Review {
    - date Date
    - int Rating
}

class Promotion {
}

class PromotionDetails {
    - float DiscountRate
    - date StartDate
    - date EndDate
}

 
Customer "1" -- "0..*" Order
Customer "*" -- "0..*" Product
Order "*" -- "*" Product
Product "1" -- "0..*" Promotion

(Order, Product) .. OrderDetails
(Product, Customer) .. Review
(Product, Promotion) .. PromotionDetails
           
@enduml
```
"""
]


