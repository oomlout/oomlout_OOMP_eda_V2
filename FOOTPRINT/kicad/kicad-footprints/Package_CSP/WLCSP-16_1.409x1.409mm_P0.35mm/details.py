
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-16_1.409x1.409mm_P0.35mm"
    hexID = "FZKCSPWLCSP16149X149P35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-16_1.409x1.409mm_P0.35mm', 'description': 'WLCSP-16, 1.409x1.409mm, 16 Ball, 4x4 Layout, 0.35mm Pitch, http://www.latticesemi.com/view_document?document_id=213', 'tags': 'CSP 16 0.35', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-16_1.409x1.409mm_P0.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-16_1.409x1.409mm_P0.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

