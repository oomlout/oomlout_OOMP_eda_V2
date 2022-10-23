
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuse_BelFuse_0ZRE0055FF_L14.0mm_W4.1mm"
    hexID = "FZKFUFUBELFUZRE55FFL14W41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuse_BelFuse_0ZRE0055FF_L14.0mm_W4.1mm', 'description': 'Fuse 0ZRE0055FF, BelFuse, Radial Leaded PTC,https://www.belfuse.com/resources/datasheets/circuitprotection/ds-cp-0zre-series.pdf', 'tags': '0ZRE BelFuse radial PTC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_BelFuse_0ZRE_0ZRE0055FF_L14.0mm_W4.1mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuse_BelFuse_0ZRE0055FF_L14.0mm_W4.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

