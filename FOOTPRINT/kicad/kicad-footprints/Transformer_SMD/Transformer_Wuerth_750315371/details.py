
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Wuerth_750315371"
    hexID = "FZKTRSMTRWUERTH75315371"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Wuerth_750315371', 'description': 'Power Transformer, horizontal core with bobbin, 6 pin, 2.54mm pitch, 11.24mm row spacing, 12.6x8.3x4.1mm', 'tags': 'transformer flyback', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Wuerth_750315371.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Wuerth_750315371')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

