
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "MAPBGA_9x9mm_Layout17x17_P0.5mm"
    hexID = "FZKBGAMAPBGA9X9LAYOUT17X17P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MAPBGA_9x9mm_Layout17x17_P0.5mm', 'description': 'MAPBGA 9x9x1.11 PKG, 9.0x9.0mm, 272 Ball, 17x17 Layout, 0.5mm Pitch, https://www.nxp.com/docs/en/package-information/98ASA00869D.pdf#page=1', 'tags': 'BGA 272 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/MAPBGA_9x9mm_Layout17x17_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : MAPBGA_9x9mm_Layout17x17_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

