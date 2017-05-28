# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#VARIANZRECHNER:
UL=[1,2,3,4,5,4,5,6,5,6,7,4,5,8,7,9]
LL=[]

summe=UL[0]
for i in UL[1:]:
    summe=summe+i
    LL.append(summe)
mean=summe/len(UL)
LL2=[]
qsumme=UL[0]
for i in UL [1:]:
    qsumme=qsumme+i*i
    LL2.append(qsumme)
Var=(qsumme/len(UL))-(mean*mean)
import math
d=math.sqrt(Var)
print(d)

#Varianz berechnet mit dem Verschiebungssatz
#Alle Listenelemente wurden aufaddiert und in neue Liste abgespeichert
#Durch Anzahl der Listenelemente geteilt (ergibt arithmetisches Mittel)
#Alle Listenelemente quadriert und anschließend addiert
#Quadrierte, addierte Listenelemente - quadriertes arithmetisches Mittel= Varianz
#Mathefunktionen importieren für die Wurzel
#Wurzel aus der Varianz ziehen für Standartabweichung
