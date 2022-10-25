
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "CYBLE-21Pin-10x10mm"
    hexID = "FZKRFMOCYBLE21PIN1X1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CYBLE-21Pin-10x10mm', 'description': 'Cypress EZ-BLE PRoC Module (Bluetooth Smart) 21 Pin Module', 'tags': 'Cypress BT Bluetooth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/CYBLE-21Pin-10x10mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : CYBLE-21Pin-10x10mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

