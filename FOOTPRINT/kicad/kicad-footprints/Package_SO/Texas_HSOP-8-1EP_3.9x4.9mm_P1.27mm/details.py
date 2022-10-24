
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Texas_HSOP-8-1EP_3.9x4.9mm_P1.27mm"
    hexID = "FZKSOTEXASHS81EP39X49P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_HSOP-8-1EP_3.9x4.9mm_P1.27mm', 'description': 'Texas Instruments HSOP 9, 1.27mm pitch, 3.9x4.9mm body, exposed pad, DDA0008J (http://www.ti.com/lit/ds/symlink/tps5430.pdf)', 'tags': 'HSOP 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSOP-8-1EP_3.9x4.9mm_Pitch1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Texas_HSOP-8-1EP_3.9x4.9mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

