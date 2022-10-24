
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65"
    hexID = "FZKSONWSON121EP3X2P5EP1X265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65', 'description': 'WSON-12 http://www.ti.com/lit/ds/symlink/lm27762.pdf', 'tags': 'WSON-12', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

