
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_01005_0402Metric_Pad0.57x0.30mm_HandSolder"
    hexID = "FZKDIODESMD1542METRICPAD57X3HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_01005_0402Metric_Pad0.57x0.30mm_HandSolder', 'description': 'Diode SMD 01005 (0402 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: http://www.vishay.com/docs/20056/crcw01005e3.pdf), generated with kicad-footprint-generator', 'tags': 'diode handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_01005_0402Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Diode_SMD : D_01005_0402Metric_Pad0.57x0.30mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

