
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_WS2812B-2020_PLCC4_2.0x2.0mm"
    hexID = "FZKLSMLWS2812B22PLCC42X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_WS2812B-2020_PLCC4_2.0x2.0mm', 'description': 'Addressable RGB LED NeoPixel Nano, 12 mA, https://cdn-shop.adafruit.com/product-files/4684/4684_WS2812B-2020_V1.3_EN.pdf', 'tags': 'LED RGB NeoPixel Nano 2020', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_WS2812B-2020_PLCC4_2.0x2.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_WS2812B-2020_PLCC4_2.0x2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

