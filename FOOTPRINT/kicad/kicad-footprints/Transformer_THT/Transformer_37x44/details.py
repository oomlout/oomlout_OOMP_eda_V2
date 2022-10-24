
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_37x44"
    hexID = "FZKTRTR37X44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_37x44', 'description': 'transformer 37x44mm²', 'tags': 'transformer 37x44mm²', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_37x44.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_37x44')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

