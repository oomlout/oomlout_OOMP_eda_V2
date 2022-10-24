
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm"
    hexID = "FZKBGATEXASMSTARJUNIORBGA1137X7LAYOUT12X12P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm', 'description': 'Texas Instruments, BGA Microstar Junior, 7x7mm, 113 ball 12x12 grid, NSMD pad definition (http://www.ti.com/lit/ml/mpbg674/mpbg674.pdf, http://www.ti.com/lit/wp/ssyz015b/ssyz015b.pdf)', 'tags': 'Texas_Junior_BGA-113', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

