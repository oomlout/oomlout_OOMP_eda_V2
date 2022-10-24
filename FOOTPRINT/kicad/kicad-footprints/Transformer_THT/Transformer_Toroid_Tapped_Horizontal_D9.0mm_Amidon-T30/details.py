
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Toroid_Tapped_Horizontal_D9.0mm_Amidon-T30"
    hexID = "FZKTRTRTOROIDTAPPEDHORIZONTALD9AMIDONT3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Toroid_Tapped_Horizontal_D9.0mm_Amidon-T30', 'description': 'Transformer, Toroid, tapped, horizontal, laying, Diameter 9mm, Amidon, T30,', 'tags': 'Transformer Toroid tapped horizontal laying Diameter 9mm Amidon T30 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Toroid_Tapped_Horizontal_D9.0mm_Amidon-T30.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_Toroid_Tapped_Horizontal_D9.0mm_Amidon-T30')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

