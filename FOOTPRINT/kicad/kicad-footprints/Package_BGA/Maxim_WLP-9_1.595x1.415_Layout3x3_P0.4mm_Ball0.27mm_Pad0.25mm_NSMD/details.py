
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Maxim_WLP-9_1.595x1.415_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm_NSMD"
    hexID = "FZKBGAMAXIMWLP91595X1415LAYOUT3X3P4BALL27PAD25NSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Maxim_WLP-9_1.595x1.415_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm_NSMD', 'description': 'Maxim_WLP-9 W91C1+1 https://pdfserv.maximintegrated.com/package_dwgs/21-0459.PDF', 'tags': 'Maxim_WLP-9', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Maxim_WLP-9_1.595x1.415_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm_NSMD.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Maxim_WLP-9_1.595x1.415_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm_NSMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

