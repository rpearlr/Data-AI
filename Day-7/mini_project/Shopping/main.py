from decorator import user_valid
import add_cart
import display_cart
@user_valid
def user_validate() :
    print("Logged In")

cart = add_cart.addcart()
display_cart.display(cart)