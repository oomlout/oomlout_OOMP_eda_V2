
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_Shunt_Vishay_WSKW0612"
    hexID = "FZKRESISTORSMRSHUNTVISHAYWSKW612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Shunt_Vishay_WSKW0612', 'description': 'https://www.vishay.com/docs/30332/wskw0612.pdf', 'tags': '4-Terminal SMD Shunt', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Shunt_Vishay_WSKW0612.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_Shunt_Vishay_WSKW0612')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

