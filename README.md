# Solve Wordscapes

My wife got my hook on the game wordscapes on our iPhones.

I will continue to play without this program, but, I figured it would be really easy to 'beat' the game with a quick python program.

The key is two python libraries:  PyEnchant (relies on the Enchant C library) and 'itertools' from the Python standard library.

https://pyenchant.github.io/pyenchant/install.html

To run on a Mac:

```bash
brew install enchant
pipenv shell
pipenv install
python solve.py [mycharacters]
```

That's it! The output looks something like this:

```bash
$ python solve.py renegt
All permutations
egret
enter
ere
erg
gee
gen
gene
genre
gent
get
green
greet
nee
neg
net
reg
regent
rent
rte
tee
teen
ten
tern
tree


```
