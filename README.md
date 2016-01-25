# BLE_Projet
BLueZ
===============================
Télécharger la derniére version de  BlueZ   <b>www.bluez.org</b>.

<code>$ wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.11.tar.gz</code></pre>

Extraire BlueZ.

<code>$ tar xvfJ bluez-5.11.tar.xz</code></pre> 
<code>$ cd bluez-5.11</code></pre>   
<code>$ ./configure --disable-systemd</code></pre>   
<code>$ make</code></pre>   
<code>$ make install</code></pre>  

SCAN BLUETOOTH LOW ENERGY
===============================
Trouver le sensorTag  
<code>$ hcitool lescan</code></pre>

B0:B4:48:BF:DA:06 (unknown)  
B0:B4:48:BF:DA:06 SensorTag  

Activer le périphérique BLE de votre machine  
<code>$sudo hciconfig</code></pre>  
<code>$sudo haciconfig hci1 up</code></pre>


Connection au sensortag  

<code>$ gattool -i  </code></pre>          
<code>$ [LE]> connect "adresse du sentortag"  </code></pre>          

Ou  
<code> $ gatttool -b "adresse du sensortag" --interactive </code></pre>      

Identifiant et adresse des capteurs  
<code>$[CON][B0:B4:48:BF:DA:06][LE]>primary </code></pre>

Charactéristique par handle  
<code>$ char-desc 0x0028 0x0028</code></pre>  

Activer un capteur   
<code>[CON][B0:B4:48:BF:DA:06][LE]> char-write-cmd "handle (configuration) capteur" 01 </code></pre>

Lire les valeurs de retour du capteur  
<code>[CON][B0:B4:48:BF:DA:06][LE]> char-read-hnd "handle(Data) capteur" </code></pre>

Lancer sur son Linux
===============================

<code>$ git clone https://github.com/valentin9280/POO_Projet.git </code></pre>   
<code>$ cd POO_Projet  </code></pre>
<code>$ python Scan_ble.py  </code></pre>



