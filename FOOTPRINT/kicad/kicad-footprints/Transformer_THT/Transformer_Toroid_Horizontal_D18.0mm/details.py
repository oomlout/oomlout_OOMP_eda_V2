
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Toroid_Horizontal_D18.0mm"
    hexID = "FZKTRTRTOROIDHORIZONTALD18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Toroid_Horizontal_D18.0mm', 'description': 'Transformer, Toroid, tapped, horizontal, laying, Diameter 18mm, ', 'tags': 'Transformer Toroid tapped horizontal laying Diameter 18mm ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Toroid_Horizontal_D18.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_Toroid_Horizontal_D18.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

