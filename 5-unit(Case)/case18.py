b = {
    1:'bir',
    2:'ikki',
    3:'uch',
    4:"to'rt",
    5:"besh",
    6:"olti",
    7:"yetti",
    8:"sakkiz",
    9:"to'qqiz",
}
on = {
    1:"o'n",
    2:"yigirma",
    3:"o'ttiz",
    4:"qirq",
    5:"ellik",
    6:"oltmish",
    7:"yetmish",
    8:"sakson",
    9:"to'qson"
}
n = int(input('n = '))

a = ''
if n>99:
    a = b[n//100] + ' yuz'
n = n % 100
if n>9:
    a += ' ' + on[n//10%10]
n = n%10
if n>0:
    a+= ' '+b[n%100]
print(a)
    
    