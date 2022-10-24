
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-16W_5.3x10.2mm_P1.27mm"
    hexID = "FZKSOSOIC16W53X12P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-16W_5.3x10.2mm_P1.27mm', 'description': '16-Lead Plastic Small Outline (SO) - Wide, 5.3 mm Body (http://www.ti.com/lit/ml/msop002a/msop002a.pdf)', 'tags': 'SOIC 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-16W_5.3x10.2mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SOIC-16W_5.3x10.2mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

