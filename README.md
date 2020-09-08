# Feature-Kernel
Feature Kernel description and implementation details

## Compile
In order to read this paper you must compile it. This can be done by running  
```bash
make
```
To succefully run this program you need to satisfy those requirements:
 - Python 3.7 or above
 - NumPy
 - Matplotlib
 - A Latex engine
 - Make
 - latexmk
 *NOTE* this will compile to PDF.

If you don't have ```make``` and/or ```latexmk``` you can compile the paper by hand. 
First generate the images by running:
 ```bash
 python plot_initial_increase.py
 ```
 
 then compile the paper using a Latex engine (here 
 for the example ```pdflatex```)
 
```bash
pdflatex feature_kernel.tex
```
### Latex Note
This paper requires a large number of Latex Packages, so you could not be able to 
compile it using a minimal Latex installation. Nevertheless this paper does not use any
third party package, so a complete installation like texlive-full is more than enough



