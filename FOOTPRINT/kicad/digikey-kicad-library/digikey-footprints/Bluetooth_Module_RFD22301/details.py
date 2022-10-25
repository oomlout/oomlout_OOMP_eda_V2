
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Bluetooth_Module_RFD22301"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSBLUETOOTHMORFD2231"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Bluetooth_Module_RFD22301', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('digikey-footprints : Bluetooth_Module_RFD22301')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

