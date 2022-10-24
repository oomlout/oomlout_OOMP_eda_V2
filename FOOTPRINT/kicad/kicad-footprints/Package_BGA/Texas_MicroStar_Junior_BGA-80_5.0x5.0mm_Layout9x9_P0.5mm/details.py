
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm"
    hexID = "FZKBGATEXASMSTARJUNIORBGA85X5LAYOUT9X9P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm', 'description': 'Texas Instruments, BGA Microstar Junior, 5x5mm, 80 ball 9x9 grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/tlv320aic23b.pdf, http://www.ti.com/lit/wp/ssyz015b/ssyz015b.pdf)', 'tags': 'Texas_Junior_BGA-80', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

