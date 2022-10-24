
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_0201_0603Metric"
    hexID = "FZKLSML2163METRIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_0201_0603Metric', 'description': 'LED SMD 0201 (0603 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: https://www.vishay.com/docs/20052/crcw0201e3.pdf), generated with kicad-footprint-generator', 'tags': 'LED', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_0201_0603Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('LED_SMD : LED_0201_0603Metric')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

