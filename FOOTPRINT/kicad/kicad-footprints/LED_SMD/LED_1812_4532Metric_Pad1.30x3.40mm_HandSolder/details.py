
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_1812_4532Metric_Pad1.30x3.40mm_HandSolder"
    hexID = "FZKLSML18124532METRICPAD13X34HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_1812_4532Metric_Pad1.30x3.40mm_HandSolder', 'description': 'LED SMD 1812 (4532 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: https://www.nikhef.nl/pub/departments/mt/projects/detectorR_D/dtddice/ERJ2G.pdf), generated with kicad-footprint-generator', 'tags': 'LED handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_1812_4532Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('LED_SMD : LED_1812_4532Metric_Pad1.30x3.40mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

