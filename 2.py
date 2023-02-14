angka = input('masukkan angka BEBAS:')

#proses
total = 0
for digit in angka:
    total = total + int(digit)


# output 
print(total)

uang = float(input('uang:'))

#proses 
usd = 14900
rpkedolar = uang  / usd
doldecimal = round(rpkedolar, 2)

yen = 130
rpkeyen = uang  / yen
yendecimal = round(rpkeyen, 2)

euro = 16700
rpkeeuro = uang  / euro
eurdecimal = round(rpkeeuro, 2)

aud = 11500
rpkeaud = uang  / aud
auddecimal = round(rpkeaud, 2)

#output
print("rp", uang, 'usd',doldecimal , '$')
print("rp", uang, 'usd',yendecimal , 'yen')
print("rp", uang, 'usd',eurdecimal , 'euro')
print("rp", uang, 'usd',auddecimal , 'aud')