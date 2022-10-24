
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm_ThermalVia"
    hexID = "FZKDFNTEXASB3QFN141EP5X55P65THERMALVIA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm_ThermalVia', 'description': 'Texas instruments QFN Package, datasheet: https://www.ti.com/lit/ds/symlink/tpsm53602.pdf', 'tags': 'Texas instruments QFN', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm_ThermalVia')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

