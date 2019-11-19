#!/usr/bin/env python
import sys

prev_key          = "  " 
running_total = 0 
rec_count = 0 
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value     
    key_in  = key_value[0]
    value_in   = key_value[1]
    curr_key = str(key_in)

    if curr_key == prev_key or prev_key == "  ":
       if value_in !='ABC':
          running_total=running_total+int(value_in)
          prev_key = curr_key
       elif value_in == 'ABC':
          print( '%s\t%s' % (curr_key, running_total))
          prev_key = curr_key
          running_total = 0
    else:
       if value_in !='ABC':
          running_total=int(value_in)
          prev_key = curr_key
