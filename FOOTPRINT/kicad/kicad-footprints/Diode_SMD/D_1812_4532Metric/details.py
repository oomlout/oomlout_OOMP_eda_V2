
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_1812_4532Metric"
    hexID = "FZKDIODESMD18124532METRIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_1812_4532Metric', 'description': 'Diode SMD 1812 (4532 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: https://www.nikhef.nl/pub/departments/mt/projects/detectorR_D/dtddice/ERJ2G.pdf), generated with kicad-footprint-generator', 'tags': 'diode', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_1812_4532Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Diode_SMD : D_1812_4532Metric')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

