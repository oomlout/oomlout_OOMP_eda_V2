
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_Array_Convex_8x0602"
    hexID = "FZKRESISTORSMRARRAYCONVEX8X62"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Array_Convex_8x0602', 'description': 'Chip Resistor Network, ROHM MNR18 (see mnr_g.pdf)', 'tags': 'resistor array', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Array_Convex_8x0602.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_Array_Convex_8x0602')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

