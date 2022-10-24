
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Toroid_Horizontal_D10.5mm_Amidon-T37"
    hexID = "FZKTRTRTOROIDHORIZONTALD15AMIDONT37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Toroid_Horizontal_D10.5mm_Amidon-T37', 'description': 'Transformer, Toroid, horizontal, laying, Diameter 10,5mm, Amidon T37,', 'tags': 'Transformer Toroid horizontal laying Diameter 10 5mm Amidon T37 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Toroid_Horizontal_D10.5mm_Amidon-T37.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_Toroid_Horizontal_D10.5mm_Amidon-T37')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

