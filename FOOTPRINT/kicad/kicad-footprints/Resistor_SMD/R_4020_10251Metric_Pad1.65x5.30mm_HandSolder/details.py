
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_4020_10251Metric_Pad1.65x5.30mm_HandSolder"
    hexID = "FZKRESISTORSMR421251METRICPAD165X53HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_4020_10251Metric_Pad1.65x5.30mm_HandSolder', 'description': 'Resistor SMD 4020 (10251 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: http://datasheet.octopart.com/HVC0603T5004FET-Ohmite-datasheet-26699797.pdf), generated with kicad-footprint-generator', 'tags': 'resistor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_4020_10251Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_4020_10251Metric_Pad1.65x5.30mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

