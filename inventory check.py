import sys 
import pyperclip, re
import os
reload(sys) 
sys.setdefaultencoding('utf8')
#os.chdir('C:\Users\h130260\Desktop')

listre = re.compile('[PFG]+\d{7}')

shipids = open('.\\shipment manifest.csv','r').read()
ship_list = []
for id in listre.findall(shipids): 
    if id not in ship_list:
        #item = id + ','
        ship_list.append(id)
        #print id
    else:
        continue

prodids = open('.\\scanned products.csv','r').read()
prod_list = []
for id in listre.findall(prodids): 
    if id not in prod_list:
        prod_list.append(id)
        #print id
    else:
        continue
prod_list.sort()
ship_list.sort()
print '------------------product list: %i items-----------------------' \
    % (len(prod_list))
for prod in prod_list:
    print prod
print '------------------shipment list: %i items-----------------------' \
    % (len(ship_list))
for ship in ship_list:
    print ship
    
miss_prod = []
f = 1
miss_ship = []

for ship in ship_list:
    if ship not in prod_list:
        miss_prod.append(ship)
    else:
        continue
        
for prod in prod_list:
    if prod not in ship_list:
        miss_ship.append(prod)
    else:
        continue
        
if len(miss_prod) == 0:
    print '\nNo missing products found\n'
else:
    print '\nI didn\'t find the following product/s based on the manifest:'
    print miss_prod
    f = 1
if len(miss_ship) == 0:
    print '\nNo missing shipment barcodes\n'
else:
    print '\nI found products not found on the manifest:'
    print miss_ship
    f = 1
    print '\n'
    
while f == 1:
    file=open('.\\results.csv', 'w')
    file.write('missing products:\n')
    list = ','.join(miss_prod)
    file.write(str(list))
    file.write('\nmissing manifest codes:\n')
    list = ','.join(miss_ship)
    file.write(str(list))
    file.close()
    print 'results.txt written to desktop\n'
    f = 0
    
input('Press ENTER to exit')