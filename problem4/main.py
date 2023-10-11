'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''


harga_product = 37000
diskon = (15/100) * harga_product
harga_akhir = harga_product - diskon
print(harga_akhir)


print("harga yang harus dibayar adalah Rp. " + str(harga_akhir))