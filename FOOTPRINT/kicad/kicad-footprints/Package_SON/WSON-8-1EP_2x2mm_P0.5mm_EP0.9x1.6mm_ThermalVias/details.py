
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias"
    hexID = "FZKSONWSON81EP2X2P5EP9X16THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias', 'description': '8-Lead Plastic WSON, 2x2mm Body, 0.5mm Pitch, WSON-8, http://www.ti.com/lit/ds/symlink/lm27761.pdf', 'tags': 'WSON 8 1EP ThermalVias', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

