
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_QFN_3.3x3.3mm_P0.65mm"
    hexID = "FZKDIODESMDQFN33X33P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_QFN_3.3x3.3mm_P0.65mm', 'description': 'QFN, diode, 3.3x3.3x1mm (https://www.wolfspeed.com/media/downloads/846/C3D1P7060Q.pdf)', 'tags': 'diode qfn 3.3', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_QFN_3.3x3.3mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : D_QFN_3.3x3.3mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

