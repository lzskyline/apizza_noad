#-*- coding: UTF-8 -*-
import os,sys,re,thread,threading

if __name__ == "__main__":
    print """
 =================================
|                                 |
|   Name:    Apizza Remove Ad     |
|   Author:  LzSkyline            |
|   WebSite: LzSkyline.com        |
|                                 |
 =================================
"""
    if len(sys.argv)<2:
        exit('You must provide at least one argument. ')
    fpath = sys.argv[1]
    if not os.path.isfile(fpath):
        exit("The file seems not exist. ")
    fopen = open(fpath)
    sname=re.match(r'(.*)\.[^\.]+$',fpath).group(1)
    if os.path.isfile(sname+'_noad.html'):
        choose = raw_input("""
The results file is already existed. \n
Do you want to rewrite it? (n=NO,default=YES):
""")
        if choose=='n':
            exit("Good bye~")
    fsave = open(sname+'_noad.html','w')
    flist=set([])
    content=fopen.read()
    c = re.compile(r'<(.*apizza.*)|(\n.*在线编辑\n.*)>')
    fsave.write(c.sub('',content))
    fsave.close()
    print "The content is saved in '"+sname+"_noad.html'"
