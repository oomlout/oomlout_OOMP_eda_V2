
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Wuerth_760871131"
    hexID = "FZKTRTRWUERTH76871131"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Wuerth_760871131', 'description': 'Transformer, horizontal core with bobbin, 14 pin, 2.49 mm pitch, 20 mm row spacing, 25x22.2x16mm https://www.we-online.com/catalog/datasheet/760871131.pdf', 'tags': 'transformer flyback', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Wuerth_760871131.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Transformer_THT : Transformer_Wuerth_760871131')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

