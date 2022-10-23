# Context managers

In this task you will need to create an instance of the `VeryPowerHungryResource` and call the `do_work` method on it. This class though is not that simple, it controls a very power hungry resource it in order to start operating on it we should first call `open` method. Since every second we keep this resource open we are wasting power we would want to close this resource as soon as possible. But there is a twist - method could potentially raise any number of exceptions. If that happens we still to responsibly call to `close` method to close the resource.  


## Exercises

### 1. Using `try...finally` construct a new `VeryPowerHungryResource`, and perform work using it.  
### 2. Implement context manager as a class.
### 3. Implement context manager as a function.
