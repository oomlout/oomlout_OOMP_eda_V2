
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_LiteOn_LTST-S326"
    hexID = "FZKLSMLLITEONLTSTS326"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_LiteOn_LTST-S326', 'description': 'http://optoelectronics.liteon.com/upload/download/DS22-2000-287/LTST-S326KGJRKT.PDF', 'tags': 'LED SMD right angle  CCA', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_LiteOn_LTST-S326.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_LiteOn_LTST-S326')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

