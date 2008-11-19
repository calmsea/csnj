#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#

import os
import cgi
import cgitb; cgitb.enable()

class UserAgent(object):
    types = dict(other = 0,
                 docomo = 1,
                 au = 2,
                 softbank = 3,)
    types_mobile  = (types[s] for s in ("docomo", "au", "softbank"))
    def __init__(self, ua=None):
        if ua is None:
            ua = os.environ.get("HTTP_USER_AGENT", "")
        self.type = self.parse(ua.lower())
        self.ua = ua
        
    def parse(self, ua):
        if ua.startswith("docomo"):
            return self.types["docomo"]
        elif ua.startswith("kddi") or ua.startswith("up"):
            return self.types["au"]
        elif (ua.startswith("softbank") or ua.startswith("vodafone") 
              or ua.startswith("MOT") or ua.startswith("j-phone")):
            return self.types["softbank"]
        else:
            return self.types["other"]

    def isDocomo(self):
        return self.type == self.types["docomo"]
    def isAu(self):
        return self.type == self.types["au"]
    def isSoftbank(self):
        return self.type == self.types["softbank"]
    def isMobile(self):
        return self.type in self.types_mobile
    
    def __str__(self):
        if self.isDocomo():
            return "DoCoMo"
        elif self.isAu():
            return "au by KDDI"
        elif self.isSoftbank():
            return "Softbank"
        return "PC(%s) - %s" % (self.type, self.ua)

ua = UserAgent()
title = "Portal Page"

print 'Content-Type: application/xhtml+xml\n'
print '<?xml version="1.0" encoding="UTF-8"?>'
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.0//EN" "http://www.w3.org/TR/xhtml-basic/xhtml-basic10.dtd">'
print '<html><head>'
print '<title>%s</title>' % title
print '</head><body>'
print "<p>This is %s</p>" % ua 
print "</body></html>"

#
# EOF
#
