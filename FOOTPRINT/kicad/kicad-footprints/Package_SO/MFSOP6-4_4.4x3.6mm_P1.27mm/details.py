
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MFSOP6-4_4.4x3.6mm_P1.27mm"
    hexID = "FZKSOMFS6444X36P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MFSOP6-4_4.4x3.6mm_P1.27mm', 'description': 'https://toshiba.semicon-storage.com/ap-en/design-support/package/detail.4pin%20MFSOP6.html', 'tags': 'MFSOP 4 pin SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MFSOP6-4_4.4x3.6mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : MFSOP6-4_4.4x3.6mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

