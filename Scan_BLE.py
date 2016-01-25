#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import pexpect
import urllib2
import urllib

#Adresse MAC du TagSensor
ble_addr ="B0:B4:48:BF:DA:06"

#Fonction de transformation de valeur hexa en float
def floatfromhex(h):
    t = float.fromhex(h)
    if t > float.fromhex('7FFF'):
        t = -(float.fromhex('FFFF') - t)
        pass
    return t


#Classe sensorTag
class sensorTag:

    #Constructeur
    def __init__(self,ble_addr):
        self.ble_addr = ble_addr
        self.child =pexpect.spawn('gatttool -b  ' + ble_addr +  '  --interactive')
        #self.child.expect('[LE]>')
        print "Tentative de connection au sensorTag"
        self.child.sendline('connect')
        self.child.expect('[CON].*>')
        print "CONNECTION"
        return

    #Capteur de la temperature IR
    def get_IRtmp(self):
        #Activer la sonde
        self.child.sendline ('char-write-cmd 0x24 01')
        #self.child.expect('[LE]>')
        self.child.sendline ('char-read-hnd 0x21')
        self.child.expect('descriptor: .*')
        rval=self.child.after.split()
        objT = floatfromhex(rval[2] + rval[1])
        ambT = floatfromhex(rval[4] + rval[3])
        #Desactive la sonde
        #self.child.sendline('char-write-cmd 0x24 00')
        return(self.IRTmp(objT, ambT))


    #Capteur d humidite
    def get_HUM(self):
        # Activer la sonde
        self.child.sendline('char-write-cmd 0x2C 01')
        # self.child.expect('[LE]>')
        self.child.sendline('char-read-hnd 0x29')
        self.child.expect('descriptor: .*')
        rval=self.child.after.split()
        #print rval
        t = floatfromhex(rval[2]+rval[1])
        h = floatfromhex(rval[4]+rval[3])
        #Desactiver la sonde
        #self.child.sendline('char-write-cmd 0x29 00')
        return(self.HUMtmp(t),self.HUMhum(h))


    #Capteur optique
    def get_OPTI(self):
        #Recuperation valeur de luminosite
        self.child.sendline('char-write-cmd 0x44 01')
        #Active la lecture des datas
        #self.child.expect('[LE]>')
        self.child.sendline('char-read-hnd 0x41')
        self.child.expect('descriptor: .*')
        rval=self.child.after.split()
        #print rval
        L = int(rval[2] + rval[1],16)
        return (self.CAPTop(L))

    #Calcul de la temperature par le capteur IR
    def IRTmp(self,objT,ambT):
        SCALE_LSB = 0.03125;
        it = int(objT) >> 2;
        t = float(it) * SCALE_LSB;
        tObj = t;
        it = int(ambT) >> 2;
        t = float(it);
        tTgt = t * SCALE_LSB;
        return tObj

    # Calcul de la temperature par le capteur d humidite
    def HUMtmp(self,temp):
        t = temp / 65536*165 - 40;
        return t

    #Calcul de l humidite
    def HUMhum(self,hum):
        hum = float(int(hum) & ~0x0003);
        h = -12 + 125.0/65536.0 * hum
        #print "%.2f pourcents" % h
        return abs(h)


    #Calcul de la luminosite
    def CAPTop(self,lux):
        m = lux & 0x0FFF;
        e = (lux& 0xF000) >> 12;
        return m * (0.01 * pow(2.0,e));



  #----------------------------------------------FONCTION PRINCIPALE----------------------------------------------#


def main():

    #Instance de connection
    sensortag=sensorTag(ble_addr)

    while True:
        #Recuperation de la temperature infra rouge
        tmpIR=sensortag.get_IRtmp()
        print "TmpIR : %.2f" % tmpIR


        #Recuperation de la temperature et l humidite
        TabHUM=[]
        TabHUM=sensortag.get_HUM()
        print "TmpHUM : %.2f" % TabHUM[0]
        print "HUM  :%.2f pourcents" % TabHUM[1]

        #Recuperation de la luminosite
        LUX=sensortag.get_OPTI()
        print "LUX : %.2f" % LUX

        time.sleep(2)
if __name__ == "__main__":

        main()


