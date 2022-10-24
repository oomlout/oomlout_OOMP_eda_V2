
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_1218_3246Metric"
    hexID = "FZKRESISTORSMR12183246METRIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_1218_3246Metric', 'description': 'Resistor SMD 1218 (3246 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: https://www.vishay.com/docs/20035/dcrcwe3.pdf), generated with kicad-footprint-generator', 'tags': 'resistor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_1218_3246Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_1218_3246Metric')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

