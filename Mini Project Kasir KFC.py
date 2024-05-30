menu = {
  "Fun Fries": 24.546,
  "Chick Ball": 14.091,
  "Winger Spice": 24.545,
  "Yakiniku Don": 15.454,
  "Oriental Don": 15.454,
  "Don's With Egg": 19.091,
  "Ala Carte Egg": 10.909,
  "Fried Chicken": 18.182,
  "Chicken Strips": 17.728,
  "KFC Winger": 21.818,
  "Chicken Balls": 12.273,
  "Colonel Burger": 25.454,
  "Burger Single": 26.819,
  "Spaghetti VIP": 10.909,
  "Burger Double": 35.910,
  "Fish Burger": 25.910,
  "Chicken Skin": 15.091,
  "Crispy Burger": 15.909,
  "Fried Twisty": 17.728,
  "Spaghetti VVIP": 19.999,
  "Cream Soup": 10.455,
  "KFC Soup": 10.455,
  "Chick Porridge": 18.636,
  "OR Porridge": 10.909,
  "F. Fries Large": 23.637,
  "French Fries": 19.091,
  "White Rice": 9.546,
  "Perkedel": 9.546,
  "Avocado Float": 15.454,
  "Mocha Float": 15.454,
  "Yubari Float": 15.454,
  "Lovlychee Float": 11.364,
  "Mango Float": 11.364,
  "Chococha Float": 15.000,
  "Coke Medium": 11.364,
  "Sprite Medium": 11.364,
  "Fanta Medium": 11.364,
  "Mineral water": 8.637,
  "Ichi Ocha": 11.364,
  "Ovaltine": 10.455
}
print("================ Daftar Menu KFC ==================")
for i in menu:
  print("Daftar Menu : ", i,"\t Harga : ",menu[i])
print("Pembelian diatas Rp100.000,-mendapatkan diskon 15%")
print("==================================================")
beli = input("Pilih Menu: ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 100.000:
  diskon = bayar*15/100
  total = bayar - diskon
else:
  total = bayar

print("================ Detail Pembayaran ==================")
print("Menu yang dipesan          : ", beli)
print("Jumlah yang dipesan        : ", jumlah)
print("Total Biaya                : ", bayar)
print("Total biaya setelah diskon : ", total)