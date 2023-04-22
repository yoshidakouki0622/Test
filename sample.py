# -*- config: utf-8 -*-

print('HelloWorld')

import random

LINEUP ={'SSR': 0, 'SR':0, 'R':0}

print(LINEUP)

gachaCountSSR = 0
gachaCountSR = 0
gachaCountR = 0

tryNumber = 100

print('gachaCountSSR：' + str(gachaCountSSR))

for i in range(tryNumber):
    print(i)

    randGacha = random.randint(1,100)

    if randGacha < 4:
    
        gachaCountSSR += 1

    elif randGacha < 22:

        gachaCountSR += 1

    else:

        gachaCountR += 1

#print('gachaCountSSR：' + str(gachaCountSSR))
#print('gachaCountSR ：' + str(gachaCountSR))
#print('gachaCountR  ：' + str(gachaCountR))

LINEUP['SSR'] = gachaCountSSR
LINEUP['SR'] = gachaCountSR
LINEUP['R'] = gachaCountR

print(LINEUP)