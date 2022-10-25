
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "VSON-8_3.3x3.3mm_P0.65mm_NexFET"
    hexID = "FZKSONVSON833X33P65NEXFET"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VSON-8_3.3x3.3mm_P0.65mm_NexFET', 'description': '8-Lead Plastic Dual Flat, No Lead Package (MF) - 3.3x3.3x1 mm Body [VSON] http://www.ti.com/lit/ds/symlink/csd87334q3d.pdf', 'tags': 'VSON 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/VSON-8_3.3x3.3mm_P0.65mm_NexFET.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : VSON-8_3.3x3.3mm_P0.65mm_NexFET')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

