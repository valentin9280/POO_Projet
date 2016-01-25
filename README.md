# BLE_Projet
<code>uname -r</code></pre>

Tester  
BLUETOOTH LOW ENERGY SCAN
Trouver le sensorTag  
<code>$ hcitool lescan</code></pre>

B0:B4:48:BF:DA:06 (unknown)  
B0:B4:48:BF:DA:06 SensorTag  

Activer le BLE  
<code>
$ sudo hciconfig
$ sudo haciconfig hci1 up
</code></pre>

Connection au sensortag  

<code>$ gattool -i  </code></pre>
<code>$ [LE]> connect "adresse du sentortag"  </code></pre>

Ou  
<code> $ gatttool -b "adresse du sensortag" --interactive </code></pre>

Identifiant et adresse des capteurs  
<code>$[CON][B0:B4:48:BF:DA:06][LE]>primary </code></pre>

Activer un capteur  
<code>[CON][B0:B4:48:BF:DA:06][LE]> char-write-cmd "handle (configuration) capteur" 01 </code></pre>

Lire les valeurs de retour du capteur
<code>[CON][B0:B4:48:BF:DA:06][LE]> char-read-hnd "handle(Data) capteur" </code></pre>
