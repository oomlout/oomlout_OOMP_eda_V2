
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Autotransformer_Toroid_1Tap_Horizontal_D14.0mm_Amidon-T50"
    hexID = "FZKTRAUTOTRTOROID1TAPHORIZONTALD14AMIDONT5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Autotransformer_Toroid_1Tap_Horizontal_D14.0mm_Amidon-T50', 'description': 'Choke, Inductance, Autotransformer, Toroid, horizontal, laying, 1 Tap, Diameter 14mm, Amidon T50,', 'tags': 'Choke Inductance Autotransformer Toroid horizontal laying 1 Tap Diameter 14mm Amidon T50 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Autotransformer_Toroid_1Tap_Horizontal_D14.0mm_Amidon-T50.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Autotransformer_Toroid_1Tap_Horizontal_D14.0mm_Amidon-T50')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

