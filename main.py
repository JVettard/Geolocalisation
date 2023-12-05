import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

#Trouver le pays du numero
num = "+221784588305"
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")
print(localisation)

#Trouver l'operateur mobile
operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur,'fr'))

#trouver la latitude et la longitude
clef = "de5d07e1c096488cb3ba193db3b3d4ee"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
#print(reponse)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat,lng)

#creation du map
monMap = folium.Map(location=[lat,lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("map.html")