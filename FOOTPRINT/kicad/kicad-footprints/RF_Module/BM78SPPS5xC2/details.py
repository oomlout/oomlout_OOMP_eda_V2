
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "BM78SPPS5xC2"
    hexID = "FZKRFMOBM78SPPS5XC2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BM78SPPS5xC2', 'description': 'Bluetooth Dual-mode module with integral chip antenna (http://ww1.microchip.com/downloads/en/DeviceDoc/60001380C.pdf)', 'tags': 'Bluetooth BR/EDR BLE', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/BM78SPPS5xC2.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : BM78SPPS5xC2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

