
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_2225_5664Metric_Pad1.80x6.60mm_HandSolder"
    hexID = "FZKCAPACITORSMC22255664METRICPAD18X66HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_2225_5664Metric_Pad1.80x6.60mm_HandSolder', 'description': 'Capacitor SMD 2225 (5664 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size from: http://datasheets.avx.com/AVX-HV_MLCC.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_2225_5664Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_SMD : C_2225_5664Metric_Pad1.80x6.60mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

