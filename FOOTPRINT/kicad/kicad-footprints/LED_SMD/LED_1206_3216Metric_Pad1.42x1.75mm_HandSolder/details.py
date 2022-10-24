
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder"
    hexID = "FZKLSML1263216METRICPAD142X175HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder', 'description': 'LED SMD 1206 (3216 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: http://www.tortai-tech.com/upload/download/2011102023233369053.pdf), generated with kicad-footprint-generator', 'tags': 'LED handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_1206_3216Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('LED_SMD : LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

