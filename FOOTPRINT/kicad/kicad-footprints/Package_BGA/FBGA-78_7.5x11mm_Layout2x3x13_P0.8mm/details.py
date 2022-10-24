
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm"
    hexID = "FZKBGAFBGA7875X11LAYOUT2X3X13P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm', 'description': 'FBGA-78, https://www.skhynix.com/product/filedata/fileDownload.do?seq=7687', 'tags': 'FBGA-78', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

