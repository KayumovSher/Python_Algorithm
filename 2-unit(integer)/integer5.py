a = int(input('a kesma uzunligi - '))
b = int(input('b kesma uzunligi - '))

if a > b:
    martta_joylashish = a // b
    qoldiq = a % b

    print('a kesmada b ', martta_joylashish, 'ta joylashadi va', qoldiq, 'ta qoldiq qoladi.')
    
else:
    print("a kesma b kesmadan uzun bolishi kerak!")