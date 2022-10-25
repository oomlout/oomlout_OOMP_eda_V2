
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm"
    hexID = "FZKSOHTSS21EP44X65P65EP34X65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm', 'description': '20-Lead Plastic Thin Shrink Small Outline (ST)-4.4 mm Body [HTSSOP], with thermal pad with vias', 'tags': 'HTSSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

