
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_3220_8050Metric"
    hexID = "FZKDIODESMD32285METRIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_3220_8050Metric', 'description': 'Diode SMD 3220 (8050 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size from: http://datasheets.avx.com/schottky.pdf), generated with kicad-footprint-generator', 'tags': 'diode', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_3220_8050Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Diode_SMD : D_3220_8050Metric')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

