# if __name=='__main' is used when you are importing some of the functions from other files
# It is used because if we don't write it then all the function present in the class you are importing will be called
# automatically

# When you write only the below line then all the function present in the imported file will be called
import if_name
# this will call the func greeting 2 times and suppose you do not want to call other func except greeting then?
if_name.greeting()
# for this reason we use  if main idiom in imported file
if_name.add()

