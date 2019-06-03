# aaurh
another archlinux user repository helper

simple python script that searches aur by parsing the aur website, downloads the package and optionally installs it automatically

## Install
```
git clone https://github.com/mo-pyy/aaurh.git
cd aaurh
pip install -r requirements.txt
```
Move the script somewhere on your `$PATH`, for example:
```
mv aaurh.py ~/.local/bin/aaurh
```

## Running

1. Run `aaurh packagename`
2. Results will be printed, type number of desired package
3. You will be asked to view the `PKGBUILD`, type y or n
4. If you viewed the `PKGBUILD` you will be asked if `makepkg -si` should be automatically run, type y or n
