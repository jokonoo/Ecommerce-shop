# Hello World

## E-commerce shop project

This project is my first take on writing e-commerce shop.
All available options at this moment are:

```
-Login
-Register
-Changing password
-Resetting password with mail confirmation
-Customizing Your profile with nickaname and avatar
-Checking Your orders
-Creating news as admin
-Setting shipping info
-Commenting news, editing, and deleting your comments
-Adding items to cart and removing it
-Adding opinions on items
-Checking your order on checkout page with selecting payment method, and shipping method
-Filtering items by price and category
-And a few more...
```

### Currently implementing django-allauth for registration confirmation, and all auth logic.

At first i was using django generic views like generic login, generic signup, but i decided to use django-allauth library because it's really helpful with all it's authentication logic that i would have to write on my own every time. 