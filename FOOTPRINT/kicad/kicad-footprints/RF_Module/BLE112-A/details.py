
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "BLE112-A"
    hexID = "FZKRFMOBLE112A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BLE112-A', 'description': 'Class 4 Bluetooth Module with on-board antenna', 'tags': 'Bluetooth Module', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/BLE112-A.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('RF_Module : BLE112-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

