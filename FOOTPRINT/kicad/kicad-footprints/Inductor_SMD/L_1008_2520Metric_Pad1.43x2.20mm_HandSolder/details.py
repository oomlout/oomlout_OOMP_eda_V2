
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_1008_2520Metric_Pad1.43x2.20mm_HandSolder"
    hexID = "FZKINDUCTORSML18252METRICPAD143X22HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_1008_2520Metric_Pad1.43x2.20mm_HandSolder', 'description': 'Inductor SMD 1008 (2520 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: https://ecsxtal.com/store/pdf/ECS-MPI2520-SMD-POWER-INDUCTOR.pdf), generated with kicad-footprint-generator', 'tags': 'inductor handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_1008_2520Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_1008_2520Metric_Pad1.43x2.20mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

