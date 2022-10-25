
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Bluetooth_Module_BLE113-A-M256K"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSBLUETOOTHMOBLE113AM256K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Bluetooth_Module_BLE113-A-M256K', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('digikey-footprints : Bluetooth_Module_BLE113-A-M256K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

