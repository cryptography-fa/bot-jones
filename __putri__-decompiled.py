# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
b = '\x1b[34;1m'
m = '\x1b[31;1m'
k = '\x1b[33;1m'
h = '\x1b[32;1m'
p = '\x1b[39;1m'
pu = '\x1b[36;1m'
c = '\x1b[35;1m'
bl = '\x1b[30;1m'
import requests, os, json
__nick__ = '%s[%s\xe2\x80\xa2%s]%s' % (p, h, p, c)
__nickname__ = raw_input('%s[%s\xe2\x80\xa2%s]%sNama%s:%s ' % (p, h, p, pu, m, p))
print '%s*%sctrl + c untuk out' % (m, bl)
while 1:
    try:
        print '%s\x00\x00\x00\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac' % p
        ___messenger___ = raw_input(__nick__ + __nickname__ + '\x1b[31;1m: \x1b[32;1m')
        __enter_your__link__ = 'https://wsapi.simsimi.com/190410/talk'
        __data_is_filed__ = '{\n\t"utext": "%s", \n\t"lang": "id" \n}' % ___messenger___
        ___controller__is_worked___ = {'Content-Type': 'application/json', 'x-api-key': 'g1MXbNhGYxfWJreNLDRz9voXojyp5xGiiaqq3v9d'}
        respon = requests.request('POST', __enter_your__link__, data=__data_is_filed__, headers=___controller__is_worked___)
        y = json.loads(respon.text)
        print '%s[%s+%s]%sPutri%s: %s' % (p, h, p, pu, m, p) + y['atext']
        print '%s\x00\x00\x00\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac' % p
        print
    except KeyboardInterrupt:
        print '\n%sBye *_*' % p
        exit()