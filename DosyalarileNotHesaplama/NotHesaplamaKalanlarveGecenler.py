Kalanlar = []
Gecenler = []


def not_hesaplama(satir):

	satir = satir[:-1]

	liste = satir.split(",")

	isim = liste[0]

	not1 = int(liste[1])

	not2 = int(liste[2])

	not3 = int(liste[3])

	not_ort = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

	if (not_ort >= 90):
		harf = "AA"
	elif (not_ort >= 85):
		harf = "BA"
	elif (not_ort >= 80):
		harf = "BB"
	elif (not_ort >= 75):
		harf = "CV"
	elif (not_ort >= 70):
		harf = "CC"
	elif (not_ort >= 65):
		harf = "DC"
	elif (not_ort >= 60):
		harf = "DD"
	elif (not_ort >= 55):
		harf = "FD"
	else:
		harf = "FF"

	if (not_ort >= 55):
		Gecenler.append(isim + " ------> " + "Not Ortalaması : " +
		                str(not_ort) + " ------> " + harf + "\n")
	else:
		Kalanlar.append(isim + " ------> " + "Not Ortalaması : " +
		                str(not_ort) + " ------> " + harf + "\n")

	return isim + " ------> " + "Not Ortalaması : " + str(not_ort) + " ------> " + harf + "\n"


with open("isim-not.txt", "r", encoding="utf-8") as file:

	eklenecekler_listesi = []
	for i in file:
		eklenecekler_listesi.append(not_hesaplama(i))

	with open("Harf-Not.txt", "w", encoding="utf-8") as file2:

		for i in eklenecekler_listesi:
			file2.write(i)
	with open("Gecenler.txt", "w", encoding="utf-8") as file3:
		for i in Gecenler:
			file3.write(i)
	with open("Kalanlar.txt", "w", encoding="utf-8") as file4:
		for i in Kalanlar:
			file4.write(i)
