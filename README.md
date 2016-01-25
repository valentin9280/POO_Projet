# BLE_Projet
<code>uname -r</code></pre>

Tester
Trouver le sensorTag  
<code>$ hcitool lescan</code></pre>

BLUETOOTH LOW ENERGY SCAN
B0:B4:48:BF:DA:06 (unknown)
B0:B4:48:BF:DA:06 SensorTag

Activer le BLE
<code>
$ sudo hciconfig
$ sudo haciconfig hci1 up
</code></pre>

Connection au sensortag
<code>
$ gattool -i
$ [LE]> connect "adresse du sentortag"
</code></pre>

Ou
<code> $ gatttool -b "adresse du sensortag" --interactive </code></pre>

Identifiant et adresse des cpateurs
$[CON][B0:B4:48:BF:DA:06][LE]>primary

Activer un capteur
[CON][B0:B4:48:BF:DA:06][LE]> char-write-cmd "handle 01



[   ][90:59:AF:0A:A8:4E][LE]> connect
[CON][90:59:AF:0A:A8:4E][LE]> char-read-hnd 0x25
[CON][90:59:AF:0A:A8:4E][LE]>
Characteristic value/descriptor: 00 00 00 00
[CON][90:59:AF:0A:A8:4E][LE]> char-write-cmd 0x29 01
[CON][90:59:AF:0A:A8:4E][LE]> char-read-hnd 0x25
[CON][90:59:AF:0A:A8:4E][LE]>
Characteristic value/descriptor: a3 ff 7c 06
[   ][90:59:AF:0A:A8:4E][LE]>
