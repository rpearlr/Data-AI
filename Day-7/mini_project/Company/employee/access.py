from decorators.access import user_valid,registration

@registration
def user_register(name,passowrd,phone) :
    print("You have successfully regitered")
  
@user_valid  
def user_validate(user,password):
    print("You have logged in")