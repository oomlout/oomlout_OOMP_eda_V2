
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_SK6812_PLCC4_5.0x5.0mm_P3.2mm"
    hexID = "FZKLSMLSK6812PLCC45X5P32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_SK6812_PLCC4_5.0x5.0mm_P3.2mm', 'description': 'https://cdn-shop.adafruit.com/product-files/1138/SK6812+LED+datasheet+.pdf', 'tags': 'LED RGB NeoPixel', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_SK6812_PLCC4_5.0x5.0mm_P3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_SK6812_PLCC4_5.0x5.0mm_P3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

