
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm"
    hexID = "FZKLSMLSK6812MPLCC435X35P175"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm', 'description': 'https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf', 'tags': 'LED RGB NeoPixel Mini', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

