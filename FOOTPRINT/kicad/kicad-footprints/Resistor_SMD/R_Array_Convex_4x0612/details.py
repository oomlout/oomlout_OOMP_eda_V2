
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_Array_Convex_4x0612"
    hexID = "FZKRESISTORSMRARRAYCONVEX4X612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Array_Convex_4x0612', 'description': 'Precision Thin Film Chip Resistor Array, VISHAY (see http://www.vishay.com/docs/28770/acasat.pdf)', 'tags': 'resistor array', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Array_Convex_4x0612.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_Array_Convex_4x0612')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

