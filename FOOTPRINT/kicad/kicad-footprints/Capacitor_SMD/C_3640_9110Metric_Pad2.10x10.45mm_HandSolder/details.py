
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_3640_9110Metric_Pad2.10x10.45mm_HandSolder"
    hexID = "FZKCAPACITORSMC364911METRICPAD21X145HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_3640_9110Metric_Pad2.10x10.45mm_HandSolder', 'description': 'Capacitor SMD 3640 (9110 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size from: http://datasheets.avx.com/AVX-HV_MLCC.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_3640_9110Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_SMD : C_3640_9110Metric_Pad2.10x10.45mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

