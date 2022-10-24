
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSOP-I-32_18.4x8mm_P0.5mm"
    hexID = "FZKSOTSI32184X8P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOP-I-32_18.4x8mm_P0.5mm', 'description': 'TSOP I, 32 pins, 18.4x8mm body (https://www.micron.com/~/media/documents/products/technical-note/nor-flash/tn1225_land_pad_design.pdf, http://www.fujitsu.com/downloads/MICRO/fma/pdfmcu/f32pm25.pdf)', 'tags': 'TSOP I 32', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-32_18.4x8mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TSOP-I-32_18.4x8mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

