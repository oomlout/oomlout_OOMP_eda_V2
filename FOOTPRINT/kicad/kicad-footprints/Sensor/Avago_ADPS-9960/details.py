
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "Avago_ADPS-9960"
    hexID = "FZKSENAVAGOADPS996"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Avago_ADPS-9960', 'description': 'Digital Proximity, Ambient Light, RGB and Gesture Sensor (https://docs.broadcom.com/doc/AV02-4191EN)', 'tags': 'DFN Sensor optical IR', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Avago_ADPS-9960.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor : Avago_ADPS-9960')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

