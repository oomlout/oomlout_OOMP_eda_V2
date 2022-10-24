
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "Analog_LFCSP-8-1EP_3x3mm_P0.5mm_EP1.53x1.85mm"
    hexID = "FZKCSPANALOGLFCSP81EP3X3P5EP153X185"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Analog_LFCSP-8-1EP_3x3mm_P0.5mm_EP1.53x1.85mm', 'description': 'LFCSP, exposed pad, Analog Devices (http://www.analog.com/media/en/technical-documentation/data-sheets/ADL5542.pdf)', 'tags': 'LFCSP 8 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-8-1EP_3x3mm_P0.5mm_EP1.53x1.85mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : Analog_LFCSP-8-1EP_3x3mm_P0.5mm_EP1.53x1.85mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

