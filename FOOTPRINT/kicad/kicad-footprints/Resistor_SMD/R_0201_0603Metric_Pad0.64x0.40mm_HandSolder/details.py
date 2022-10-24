
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_0201_0603Metric_Pad0.64x0.40mm_HandSolder"
    hexID = "FZKRESISTORSMR2163METRICPAD64X4HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_0201_0603Metric_Pad0.64x0.40mm_HandSolder', 'description': 'Resistor SMD 0201 (0603 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: https://www.vishay.com/docs/20052/crcw0201e3.pdf), generated with kicad-footprint-generator', 'tags': 'resistor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_0201_0603Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_0201_0603Metric_Pad0.64x0.40mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

