
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_LiteOn_LTST-C19HE1WT"
    hexID = "FZKLSMLLITEONLTSTC19HE1WT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_LiteOn_LTST-C19HE1WT', 'description': 'LiteOn RGB LED; https://optoelectronics.liteon.com/upload/download/DS22-2008-0044/LTST-C19HE1WT.pdf', 'tags': 'LED RGB Chip SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_LiteOn_LTST-C19HE1WT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_LiteOn_LTST-C19HE1WT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

