
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "MAPBGA_14x14mm_Layout17x17_P0.8mm"
    hexID = "FZKBGAMAPBGA14X14LAYOUT17X17P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MAPBGA_14x14mm_Layout17x17_P0.8mm', 'description': 'MAPBGA 14x14x1.18 PKG, 14.0x14.0mm, 289 Ball, 17x17 Layout, 0.8mm Pitch, https://www.nxp.com/docs/en/package-information/98ASA00855D.pdf#page=1', 'tags': 'BGA 289 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/MAPBGA_14x14mm_Layout17x17_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : MAPBGA_14x14mm_Layout17x17_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

