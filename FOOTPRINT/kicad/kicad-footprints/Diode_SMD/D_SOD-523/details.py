
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_SOD-523"
    hexID = "FZKDIODESMDSOD523"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_SOD-523', 'description': 'http://www.diodes.com/datasheets/ap02001.pdf p.144', 'tags': 'Diode SOD523', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SOD-523.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : D_SOD-523')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

