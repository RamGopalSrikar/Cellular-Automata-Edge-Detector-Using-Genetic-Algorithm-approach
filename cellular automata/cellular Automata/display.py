# -*- coding: utf-8 -*-

from tabulate import tabulate
with open("solution.json",'r') as f:
  table = json.loads(f.read());
  
tabulate(table,['state','rule'])

