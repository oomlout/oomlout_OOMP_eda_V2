
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_01005_0402Metric"
    hexID = "FZKINDUCTORSML1542METRIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_01005_0402Metric', 'description': 'Inductor SMD 01005 (0402 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: http://www.vishay.com/docs/20056/crcw01005e3.pdf), generated with kicad-footprint-generator', 'tags': 'inductor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_01005_0402Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_01005_0402Metric')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

