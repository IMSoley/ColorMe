# ColorMe
Python 3 colored output, Simple script to color your python output in your projects, this script tested in **Windows 10**, **Linux**

### Usages
copy this repo and put **pycolor.py** file in your project folder(current working directory) then 
```python
from pycolor import ColorMe
```

Simply define your color
```python
# for color only
ColorMe.red('Hello World')
ColorMe.yellow('Hello World')

# color with background
ColorMe.red('Hello World', bg='yellow')

# color, background and style (bold)
ColorMe.yellow('Hello World', bg='yellow', dec='bold')

# for labels(see below table to look all supported labels)
ColorMe.warning('Hello World')

# many more.....
```

#### Try them one by one
```python
# print("I love", ColorMe.red("Panda"))
# print("I love", ColorMe.red("Panda", dec="bold"))
# print("I love", ColorMe.red("Panda", dec="bold, underline"))
# print("I love", ColorMe.red("Panda", dec="bold, underline, reversed"))
# print("I love", ColorMe.black("Panda", bg="purple"))
# print("I love", ColorMe.black("Panda", bg="purple", dec="bold"))
# print("I love", ColorMe.black("Panda", bg="purple", dec="bold, underline"))
# print("I love", ColorMe.red("Panda", bg="black", dec="bold, underline, reversed"))
# print("Name with label", ColorMe.warning(" Panda"))
# print("Name with label & color", ColorMe.info(ColorMe.green(" Panda")))
# print("I love", ColorMe.success(ColorMe.red(" Panda", dec="bold")))
```

#### Above code output from Windows cmd
![Alt text](https://i.imgur.com/K1CVWdS.png "python colored output")


### Supported colors and styles

| Background(bg)| Foreground(fg)| Style(dec) | Label(lab)  | 
| ------------- |:-------------:| ----------:| -----------:|
| black         | black         | bold       | warning
| red           | red           | underline  | info
| green         | green         | reversed   | success
| yellow        | yellow        |            | question
| blue          | blue          |            | running
| purple        | purple        |            | 
| cyan          | cyan          |            |
| white         | white         |            |


