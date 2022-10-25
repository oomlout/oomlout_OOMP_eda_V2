
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_SOD-110"
    hexID = "FZKDIODESMDSOD11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_SOD-110', 'description': 'SOD-110', 'tags': 'SOD-110', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SOD-110.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : D_SOD-110')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

