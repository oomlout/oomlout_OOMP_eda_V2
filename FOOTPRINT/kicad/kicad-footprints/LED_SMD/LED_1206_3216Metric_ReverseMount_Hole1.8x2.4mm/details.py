
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm"
    hexID = "FZKLSML1263216METRICRMOUNTHOLE18X24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm', 'description': 'LED SMD 1206 (3216 Metric), reverse mount, square (rectangular) end terminal, IPC_7351 nominal, (Body size source: http://www.tortai-tech.com/upload/download/2011102023233369053.pdf), generated with kicad-footprint-generator', 'tags': 'diode reverse', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_1206_3216Metric_ReverseMount.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('LED_SMD : LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

