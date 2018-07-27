# -*- coding: utf-8 -*-

import os
import sys

opts = ['-cell', 'DefaultCell01', '-defaultbinding.virtual.host', 'default_host', '-usedefaultbindings']

params = sys.argv

while params[0].startswith('--'):
  opts.append(params[0][1:])
  opts.append(params[1])
  params = params[2:]

total = len(params)
success = 0

for ear in params:
    print ''
    try:
      AdminApp.install(ear, opts)
      AdminConfig.save()
      success += 1
    except:
      print 'Can\'t deploy '+ear

if success < total:
   os._exit(200)
