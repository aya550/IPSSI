temp= input ("entrer la temperature que vous voulez convertir (ex: 35C ou 95F) : ")
value = float(temp[:-1])
unit = temp[-1].upper()

if unit == "F": 
  tempC= (value -32 )/ 1.8
  print ("la temperature en celsius est de :", tempC, "C")
else :
  tempF= (value * 9/5) + 32
  print ("la temperature en fahrenheit est de :", tempF, "F")

        
 