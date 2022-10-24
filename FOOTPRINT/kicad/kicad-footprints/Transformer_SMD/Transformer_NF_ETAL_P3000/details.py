
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_NF_ETAL_P3000"
    hexID = "FZKTRSMTRNFETALP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_NF_ETAL_P3000', 'description': 'NF-Reansformer, ETAL, P3000, SMD,', 'tags': 'NF-Reansformer ETAL P3000 SMD ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_NF_ETAL_P3000.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Transformer_NF_ETAL_P3000')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

