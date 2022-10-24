
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-20_1.994x1.609mm_Layout5x4_P0.4mm"
    hexID = "FZKCSPWLCSP21994X169LAYOUT5X4P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-20_1.994x1.609mm_Layout5x4_P0.4mm', 'description': 'WLCSP-20, https://www.nxp.com/docs/en/package-information/98ASA00676D.pdf', 'tags': 'WLCSP-20', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-20_1.994x1.609mm_Layout5x4_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-20_1.994x1.609mm_Layout5x4_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

