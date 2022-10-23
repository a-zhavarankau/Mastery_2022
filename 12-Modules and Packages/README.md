# Modules and Packages

In the file `main.py` you have a code that prints the contents of the directories in the tree form. You can try to run this code like this 

```bash
python main.py /path/to/directory
``` 

This code is a bit hard to read and reason about when it's all in the same file. We will try to fix that by splitting it into separate modules and creating a package with that modules.  

## Exercises
Your task is to create new package called `folder_visualizer`. In this package there should be 2 modules `cli.py` and `visualizer.py`. In `cli.py` module put the logic for parsing the command line arguments and in `visualizer.py` put logic for actually printing the folder structure. In the end the only code that should remain in your `main.py` file is the following:

```(Python)
    from folder_visualizer.cli import main

    if __name__ == "__main__":
        main()
```
