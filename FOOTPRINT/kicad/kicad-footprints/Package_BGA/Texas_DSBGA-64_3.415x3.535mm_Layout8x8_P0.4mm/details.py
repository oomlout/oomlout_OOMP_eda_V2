
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm"
    hexID = "FZKBGATEXASDSBGA643415X3535LAYOUT8X8P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm', 'description': 'Texas Instruments, DSBGA, 3.415x3.535x0.625mm, 64 ball 8x8 area grid, NSMD pad definition (http://www.ti.com/lit/ds/slas718g/slas718g.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)', 'tags': 'texas dsbga 64', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

