#-*- encoding: utf-8 -*-
#Веб-версия

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
    
    result = data[(cat,)] + "\n"
    
    if crit1 != '':
        result = result + "  " + data[(cat,crit1)] + "\n"
        if crit2 != '':
            result = result + "    " + data[(cat,crit1,crit2)] + "\n"
            if crit4 == "":
                for i in range(len(crit3)):
                    result = result + "      " + data[(cat,crit1,crit2,crit3[i])] + "\n"
            else:
                for crit3,crit4 in crit34:
                    result = result + "      " + data[(cat,crit1,crit2,crit3)] + "\n"
                    if crit4 != '':
                        for j in crit4.split(","):
                            result = result + "        " + data[(cat,crit1,crit2,crit3,j)] + "\n"
    
    result = result + "*************************************************************\n"
    
    fo.write(result)

if __name__ == '__main__':
    args = sys.argv[ 1: ]
    if args is None or len( args ) < 2:
        usage()
    
    data = iucn2text_data.iucndata()
    
    val = args[ 0 ]
    fon = args[ 1 ]
    fo = open(fon,"w")
    fo.write("Дешифрируем: " + val + "\n\n")
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
    
    fo.close()

