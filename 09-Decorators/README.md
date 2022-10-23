# Decorators
## Exercises

###1.
See the files `class_wrapper.py` and `function_wrapper.py`. There are a class `Pen` and a function `get_text` annotated with `@bold` and `@italic`. Please implement the `@bold` and `@italic` decorators in appropriate files to decorate the class and function. Be sure you are following the order in which decoration occurs. 
For example: 
```
@bold
@italic
def get_text():
    return 'The quick brown fox jumps over the lazy dog'
```

Should return `<b><i>The quick brown fox jumps over the lazy dog<\b><\i>`.