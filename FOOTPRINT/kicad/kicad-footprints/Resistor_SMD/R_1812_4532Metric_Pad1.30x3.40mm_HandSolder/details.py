
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_1812_4532Metric_Pad1.30x3.40mm_HandSolder"
    hexID = "FZKRESISTORSMR18124532METRICPAD13X34HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_1812_4532Metric_Pad1.30x3.40mm_HandSolder', 'description': 'Resistor SMD 1812 (4532 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: https://www.nikhef.nl/pub/departments/mt/projects/detectorR_D/dtddice/ERJ2G.pdf), generated with kicad-footprint-generator', 'tags': 'resistor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_1812_4532Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_1812_4532Metric_Pad1.30x3.40mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

