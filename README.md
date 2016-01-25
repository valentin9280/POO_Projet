# BLE_Projet

Tester
Trouver le sensorTag
$ hcitool lescan

BLUETOOTH LOW ENERGY SCAN
B0:B4:48:BF:DA:06 (unknown)
B0:B4:48:BF:DA:06 SensorTag

Activer le BLE
$ sudo hciconfig
$ sudo haciconfig hci1 up

Connection au sensortag
$ gattool -i
$ [LE]> connect "adresse du sentortag"

Ou
$ gatttool -b "adresse du sensortag" --interactive

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
