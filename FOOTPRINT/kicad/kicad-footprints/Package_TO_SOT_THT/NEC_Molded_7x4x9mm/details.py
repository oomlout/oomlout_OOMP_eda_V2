
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "NEC_Molded_7x4x9mm"
    hexID = "FZKSOTNECMOLDED7X4X9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'NEC_Molded_7x4x9mm', 'description': 'Molded Japan Transistor Package 7x4x9mm^3, http://rtellason.com/transdata/2sb734.pdf', 'tags': 'Japan transistor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/NEC_Molded_7x4x9mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : NEC_Molded_7x4x9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

