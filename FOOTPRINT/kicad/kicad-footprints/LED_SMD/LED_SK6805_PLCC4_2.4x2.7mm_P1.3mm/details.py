
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm"
    hexID = "FZKLSMLSK685PLCC424X27P13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm', 'description': 'https://cdn-shop.adafruit.com/product-files/3484/3484_Datasheet.pdf', 'tags': 'LED RGB NeoPixel Nano', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

