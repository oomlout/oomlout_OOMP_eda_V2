
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm"
    hexID = "FZKLSMLWS2812BPLCC45X5P32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm', 'description': 'https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf', 'tags': 'LED RGB NeoPixel', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

