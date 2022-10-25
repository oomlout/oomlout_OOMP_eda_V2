
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-56-1EP_6.1x14mm_P0.5mm_EP3.61x6.35mm"
    hexID = "FZKSOHTSS561EP61X14P5EP361X635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-56-1EP_6.1x14mm_P0.5mm_EP3.61x6.35mm', 'description': 'HTSSOP56: plastic thin shrink small outline package http://www.ti.com/lit/ds/symlink/drv8301.pdf', 'tags': 'HTSSOP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-56-1EP_6.1x14mm_P0.5mm_EP3.61x6.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : HTSSOP-56-1EP_6.1x14mm_P0.5mm_EP3.61x6.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

