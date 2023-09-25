apple_price = 2
#Berikan 10 ke variable money
money=10

input_count = input ('Mau berapa apol?: ")
count = int (input_count)    
total price apple_price* count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total price) + ' dolar')

#Tambahkan control flow berdasarkan perbandingan antara money dan total price
if(total price<money): 
print('Anda telah membeli ' +str(input_count)+ ' apel')
print('Uang Anda tinggal ' +str(total price-money)+ ' dolar' )
elif (total prices==money):
print('Anda telah membeli ' +str(input_count)+ ' apel')
print('Dompet Anda kosong')
else:
print('Ulang Anda tidak mencukupi')
print('Anda tidak dapat membeli apel sebanyak itu')
