
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm"
    hexID = "FZKBGAXFBGA3635X35LAYOUT6X6P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm', 'description': 'XFBGA-36, https://www.nxp.com/docs/en/package-information/SOT1555-1.pdf', 'tags': 'XFBGA-36', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

