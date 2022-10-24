
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSOP-I-32_18.4x8mm_P0.5mm_Reverse"
    hexID = "FZKSOTSI32184X8P5R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOP-I-32_18.4x8mm_P0.5mm_Reverse', 'description': 'TSOP I, 32 pins, 18.4x8mm body (http://www.futurlec.com/Datasheet/Memory/628128.pdf), reverse mount', 'tags': 'TSOP I 32 reverse', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-32_18.4x8mm_P0.5mm_Reverse.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TSOP-I-32_18.4x8mm_P0.5mm_Reverse')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

