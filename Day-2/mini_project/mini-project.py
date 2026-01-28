import utils

dict = utils.get_user_details()
items=utils.get_items()
utils.print_user(dict)
utils.print_final_bill(items)
path=utils.download_bill(items)
utils.make_copy_bill(path)

