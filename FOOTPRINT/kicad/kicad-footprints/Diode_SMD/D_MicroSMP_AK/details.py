
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_MicroSMP_AK"
    hexID = "FZKDIODESMDMSMPAK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_MicroSMP_AK', 'description': 'Diode MicroSMP (DO-219AD), large-pad cathode, https://www.vishay.com/docs/89020/mss1p3l.pdf', 'tags': 'Diode MicroSMP (DO-219AD)', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_MicroSMP_AK.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : D_MicroSMP_AK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

