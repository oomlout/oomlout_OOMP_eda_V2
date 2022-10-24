
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "WLP-4_0.73x0.73mm_Layout2x2_P0.35mm_Ball0.22mm_Pad0.2mm_NSMD"
    hexID = "FZKBGAWLP473X73LAYOUT2X2P35BALL22PAD2NSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLP-4_0.73x0.73mm_Layout2x2_P0.35mm_Ball0.22mm_Pad0.2mm_NSMD', 'description': 'WLP-4, 2x2 raster, 0.73x0.73mm package, pitch 0.35mm; https://datasheets.maximintegrated.com/en/ds/MAX40200.pdf', 'tags': 'BGA 4 0.35', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/WLP-4_0.73x0.73mm_Layout2x2_P0.35mm_Ball0.22mm_Pad0.2mm_NSMD.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : WLP-4_0.73x0.73mm_Layout2x2_P0.35mm_Ball0.22mm_Pad0.2mm_NSMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

