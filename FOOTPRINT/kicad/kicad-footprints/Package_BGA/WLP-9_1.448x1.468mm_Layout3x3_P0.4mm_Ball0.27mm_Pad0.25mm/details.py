
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "WLP-9_1.448x1.468mm_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm"
    hexID = "FZKBGAWLP91448X1468LAYOUT3X3P4BALL27PAD25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLP-9_1.448x1.468mm_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm', 'description': 'WLP-9, 1.448x1.468mm, 9 Ball, 3x3 Layout, 0.4mm Pitch, https://pdfserv.maximintegrated.com/package_dwgs/21-100168.PDF', 'tags': 'BGA 9 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/WLP-9_1.448x1.468mm_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : WLP-9_1.448x1.468mm_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

