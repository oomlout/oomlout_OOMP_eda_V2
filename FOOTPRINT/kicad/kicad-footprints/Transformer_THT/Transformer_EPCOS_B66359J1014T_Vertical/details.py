
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_EPCOS_B66359J1014T_Vertical"
    hexID = "FZKTRTREPCOSB66359J114TVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_EPCOS_B66359J1014T_Vertical', 'description': 'Transformer, Transformator, ETD29, 14 Pin, Vertical, EPCOS-B66359J1014T,', 'tags': 'Transformer Transformator ETD29 14 Pin Vertical EPCOS-B66359J1014T ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_EPCOS_B66359J1014T_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_EPCOS_B66359J1014T_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

