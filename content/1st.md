Title: Seting Up this blog with Pelican
Date: 2015-12-24 11:26 
Modified: 2016-01-23 10:26 
Category: non-odoo
Tags: pelican, publishing
Slug: setup-blog
Authors: Pouya MN
Summary: How did i setup this blog

Hi every body, at first it looked like this is a very easy process to setup this blog, but it wasn't that easy. 
Gitpages suggested Jekil for blog handling , but I wanted something pythonic, so I decided to use pelican. I made a first blog using the guide in github [here](https://fedoramagazine.org/make-github-pages-blog-with-pelican/). It was nice but i had a few problems, I'm using SVN normally, so I'm not very familiar with git, this was my source of problems, I guess.
The problem was about repositories, the method mentioned in that page was cool, in compare to the other and more official methods, but you have to use a submodule which was new to me. 

Ok let's cut the crap, I did this:

First I made a repository by the [official documentions](https://pages.github.com/) (I didn't install jekil). Then I created two new repositories, myusername.github.io-src and myusername.github.io, as explained on [Github pages](https://github.com/new).

Then I cloned the source (...-src) to a folder named *ghpages* by:
```bash
git clone https://github.com/myusername/myusername.github.io-src.git ghpages
```
and made git remember my creditentials:
```bash
git config credential.helper store
```
I made a submodel repository by entering this in my main folder (ghpages):

```bash
git submodule add https://github.com/pouyamn/pouyamn.github.io.git output
```
so it made a folder named *output*. Now it was the time for installing pelican and running it:
```bash
sudo apt-get install python-pelican
cd /ghpages
pelican-quickstart 
```
we have to stop pelican from erasing the output directory everytime, I edited *publishconf.py*: 
```python
DELETE_OUTPUT_DIRECTORY = False
```
well it is almost there, make the first post in contents folder. I used MarkDown, although other languages are also possible. For this I installed haroopad
```bash
sudo apt-get install haroopad
``` 
I made a file in *content* folder named for example, *first.md*. and I made this post in it.
Ok, let's take a look:
```bash
make html && make serve
```
you can now open *localhost:8000* and enjoy your first post in your pc (links willnot work, they are directed to the *real* blog). 

Publish time!
```bash
make publish
cd output/
git add .
git commit -m "First Post."
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc file
git add .
git commit -m "First commit."
git push -u origin master
```
Demystification:
make the html files, setup the links and prepare it, send the compiled result to github and finally send the source files to github too keep them safe :).
that's it.

__edit__
Some caretaker's tasks:

* Make publishing more automatic and comfortable:
```bash
#file: makefile
...
github: publish
		cd $(OUTPUTDIR)
		git -C $(OUTPUTDIR) add -A .
		git -C $(OUTPUTDIR) commit -m "Auto Post!"	
		git -C $(OUTPUTDIR) push origin master
		cd $(BASEDIR)
		git add -A .
		git commit -m "Auto Commit!"	
		git push origin master
```
So I can use `make github` for publishing and posting to my account.

* take care of `pelicanconf.py` and `publishconf.py`, the former is for local serving and testing and the latter is for publishing, as the name suggests!

 *  put disqus, google analytics etc in publish profile only, put the others in **both** .
 
 * use relative paths in `pelicanconf.py`, don't use them in `publishconf.py`.