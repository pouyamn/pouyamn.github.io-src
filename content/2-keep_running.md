Title: Keep Odoo running, easily
Date: 2016-01-12 11:26 
Modified: 2016-01-12 11:26 
Category: odoo
Tags: odoo, openerp, general 
Slug: keep-odoo-running
Authors: Pouya MN
Summary: keep odoo running even when stability is low

A few months ago we had this problem with odoo, the server was sometimes jumping out; quiting with no error, sometimes some momory error. All we had to do was running it agian. It was happening about every 12-48 hours normally but some times every 2-3 hours. It was a pain in the butt, so I made an easy solution that is still working. It means no user complains anymore ;).

A bit of history, I was using ssh to connect to the server and run it with this command:
```bash
nohup ./openerp-server &
``` 
please note that I ran ./openerep-server directly, whenever I close ssh connection the server would quit. 

The solution was a shell script. At first, I tried to check if odoo is running and if not run it. I started with this command:
```bash
#NOT WORKING
ps aux | grep openerp || echo "not running"
```
Demystification:

**ps aux** *list process and send output to screen*
**grep openerp** *filter process with openerp in them.*
**|| echo "not running"** *if the result(exit code) of grep is false, print 'not found'* 

Easy,but wait my own command is always fetch by grep! the result is 
```
my_user       4220 16.4  4.9 1080324 400516 pts/0  Sl   07:54  21:15 python ./openerp-server
my_user      32186  0.0  0.0   7836   884 pts/1    S+   10:04   0:00 grep openerp
```
So the exit code of grep is always greater than 0 or logically speeking, it is *True*. I cannot understad wether odoo is running. I had to filter out 'grep' line, or keep odoo lines only: 
```bash
ps aux | grep openerp |grep python || echo "not running"
```
Demysitification:
*firstly, filter lines with openerp in them then filter the results again by:*
**grep python** *yes, nasty 'grep' line has no python in it! ;)*

now it works fine. 
For the next step I wrote a bash script starting like:
```bash
if [ps aux | grep openerp | grep python] 
...
```
But then it downed on me that the solution is much easier, the final script is:
```bash
run-odoo.sh:

cd ~/odoo #replace it with your odoo folder
while [ : ]
do
./openerp-server
sleep 3
done
```
just run it the same as before:
```bash
nohup ./run-odoo.sh &
````
clean and easy! 