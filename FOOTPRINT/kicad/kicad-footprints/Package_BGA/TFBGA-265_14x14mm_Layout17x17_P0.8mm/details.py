
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "TFBGA-265_14x14mm_Layout17x17_P0.8mm"
    hexID = "FZKBGATFBGA26514X14LAYOUT17X17P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TFBGA-265_14x14mm_Layout17x17_P0.8mm', 'description': 'TFBGA-265, 17x17 raster, 14x14mm package, pitch 0.8mm; see section 7.8 of http://www.st.com/resource/en/datasheet/DM00387108.pdf', 'tags': 'BGA 265 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/TFBGA-265_14x14mm_Layout17x17_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : TFBGA-265_14x14mm_Layout17x17_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

