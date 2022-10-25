
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Autotransformer_Toroid_1Tap_Horizontal_D9.0mm_Amidon-T30"
    hexID = "FZKTRAUTOTRTOROID1TAPHORIZONTALD9AMIDONT3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Autotransformer_Toroid_1Tap_Horizontal_D9.0mm_Amidon-T30', 'description': 'Autotransformer, Toroid, horizontal, laying, 1 Tap, Diameter 9mm, Amidon T30,', 'tags': 'Autotransformer Toroid horizontal laying 1 Tap Diameter 9mm Amidon T30 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Autotransformer_Toroid_1Tap_Horizontal_D9.0mm_Amidon-T30.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Autotransformer_Toroid_1Tap_Horizontal_D9.0mm_Amidon-T30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

