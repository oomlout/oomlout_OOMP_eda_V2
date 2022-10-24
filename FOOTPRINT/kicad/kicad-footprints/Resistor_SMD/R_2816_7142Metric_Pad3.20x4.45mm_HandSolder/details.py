
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_2816_7142Metric_Pad3.20x4.45mm_HandSolder"
    hexID = "FZKRESISTORSMR28167142METRICPAD32X445HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_2816_7142Metric_Pad3.20x4.45mm_HandSolder', 'description': 'Resistor SMD 2816 (7142 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size from: https://www.vishay.com/docs/30100/wsl.pdf), generated with kicad-footprint-generator', 'tags': 'resistor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_2816_7142Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_2816_7142Metric_Pad3.20x4.45mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

