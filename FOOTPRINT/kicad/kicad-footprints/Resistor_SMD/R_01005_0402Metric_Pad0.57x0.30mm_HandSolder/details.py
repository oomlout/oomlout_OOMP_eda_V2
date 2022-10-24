
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_01005_0402Metric_Pad0.57x0.30mm_HandSolder"
    hexID = "FZKRESISTORSMR1542METRICPAD57X3HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_01005_0402Metric_Pad0.57x0.30mm_HandSolder', 'description': 'Resistor SMD 01005 (0402 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: http://www.vishay.com/docs/20056/crcw01005e3.pdf), generated with kicad-footprint-generator', 'tags': 'resistor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_01005_0402Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_01005_0402Metric_Pad0.57x0.30mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

