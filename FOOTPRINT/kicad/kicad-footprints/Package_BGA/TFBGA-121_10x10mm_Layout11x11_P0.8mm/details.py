
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "TFBGA-121_10x10mm_Layout11x11_P0.8mm"
    hexID = "FZKBGATFBGA1211X1LAYOUT11X11P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TFBGA-121_10x10mm_Layout11x11_P0.8mm', 'description': 'TFBGA-121, 11x11 raster, 10x10mm package, pitch 0.8mm; http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#p495', 'tags': 'BGA 121 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/TFBGA-121_10x10mm_Layout11x11_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : TFBGA-121_10x10mm_Layout11x11_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

