
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100"
    hexID = "FZKLSMLRGBWUERTHPLCC432X2815141M1731"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100', 'description': '3.2mm x 2.8mm PLCC4 LED, https://www.we-online.de/katalog/datasheet/150141M173100.pdf', 'tags': 'LED RGB Wurth PLCC-4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

