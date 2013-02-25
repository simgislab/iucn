#!/usr/local/bin/python
#-*- encoding: utf-8 -*-

import cgitb ; cgitb.enable()
import cgi

import re
import sys
import iucn2text_data

def usage():
  '''Show usage synopsis.
  '''
  #iucn2text.py "EN A2abc+3bc+4abc; B1b(iii,iv,v)+2b(iii,iv,v)c(ii,iii,iv)" iucn2text-output.txt
  print 'Usage: iucn2text.py code_to_decode output_txt_file'
  sys.exit( 1 )

def descript(cat,crit1,crit2,crit3,crit4):
    
    result = data[(cat,)] + "<br>"
    
    if crit1 != '':
        result = result + "&nbsp;&nbsp;" + data[(cat,crit1)] + "<br>"
        if crit2 != '':
            result = result + "&nbsp;&nbsp;&nbsp;&nbsp;" + data[(cat,crit1,crit2)] + "<br>"
            if crit4 == "":
                for i in range(len(crit3)):
                    result = result + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + data[(cat,crit1,crit2,crit3[i])] + "<br>"
            else:
                for crit3,crit4 in crit34:
                    result = result + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + data[(cat,crit1,crit2,crit3)] + "<br>"
                    if crit4 != '':
                        for j in crit4.split(","):
                            result = result + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + data[(cat,crit1,crit2,crit3,j)] + "<br>"
    
    result = result + "*************************************************************<br>"
    
    print(result)

if __name__ == '__main__':  
    form = cgi.FieldStorage()
    
    val = form.getvalue("iucncode") #args[ 0 ]
    
    print "Content-Type: text/html\n"
    # note the extra blank line terminate the headers
    print("Дешифрируем: " + val + "<br><br>")
    
    data = iucn2text_data.iucndata()
    
    result = ''

    #get category
    cat = val[0:2]                              #EN

    #get all criteria groups (can be multiple)
    critsall = val[3:len(val)]                  #A2abc+3bc+4abc; B1b(iii,iv,v)+2b(iii,iv,v)c(ii,iii,iv)

    critsgrps = critsall.split(";")             #A2abc+3bc+4abc, B1b(iii,iv,v)+2b(iii,iv,v)c(ii,iii,iv)
    if critsgrps != ['']:
        for critsgrp in critsgrps:                  #A2abc+3bc+4abc
            critsgrp = critsgrp.lstrip()            #A2abc+3bc+4abc
            crit1 = critsgrp[0]                     #A
            if crit1 not in "ABCDE":
                crit1 = crit1save
                critsgrp = crit1 + critsgrp
            crit1save = crit1
            
            critsgrp = critsgrp[1:len(critsgrp)]    #2abc+3bc+4abc
            
            #get all criteria blocks within group (can be multiple)
            critsgrp = critsgrp.split("+")          #2abc, 3bc, 4abc
            if critsgrp != ['']:
                for crits in critsgrp:                  #2abc
                    crit2 = crits[0]                    #2
                    
                    crit3 = crits[1:len(crits)]         #abc or b(iii,iv,v) or b(iii,iv,v)c(ii,iii,iv)
                    
                    #determine if there is 4th level
                    if "(" in crit3:
                        crit34 = map(
                                      lambda (m): tuple(map(lambda (x): x if x else '', m.groups())),
                                      re.finditer(r'(\w)(?:\((.*?)\)){0,1}', crit3)
                                    )
                        descript(cat,crit1,crit2,'777',crit34)
                    else:
                        crit4 = ""
                        descript(cat,crit1,crit2,crit3,crit4)
            else:
                descript(cat,crit1,'','','')
    else:
        descript(cat,'','','','')
    
    #fo.close()

