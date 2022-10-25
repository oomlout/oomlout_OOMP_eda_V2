
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuse_0402_1005Metric_Pad0.77x0.64mm_HandSolder"
    hexID = "FZKFUFU4215METRICPAD77X64HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuse_0402_1005Metric_Pad0.77x0.64mm_HandSolder', 'description': 'Fuse SMD 0402 (1005 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: http://www.tortai-tech.com/upload/download/2011102023233369053.pdf), generated with kicad-footprint-generator', 'tags': 'fuse handsolder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_0402_1005Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuse_0402_1005Metric_Pad0.77x0.64mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

