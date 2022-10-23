# Exceptions

## Exercises

###1. Rewriting code using Exceptions

See the code in main.py. You can see there is a small function to get some pets from the file(see the `file_db.txt`). You can start it using the command from the project directory:
`python3 main.py count` (e.g. `python3 main.py 3` if you need to get 3 pets).  

There is only one parameter `count`. Passing this parameter you can get an appropriate count of pets. Please start and test it!

Now think about what if you try to pass negative numbers for the count parameter. Try to reimplement the `get_pets` function using python Exceptions. Put it in the right places to prevent the program from bugs and simple errors such as the absence of `file_db.txt`, etc. As you can see there is some validation for the `count` parameter(you should pass it at least), so please implement your `CustomAPIException` class to use it for validation cases. What other validation cases should be handled? Please take care of it. Write your code in `main.py`. 
