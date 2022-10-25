
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-10-1EP_2x3mm_P0.5mm_EP0.84x2.4mm_ThermalVias"
    hexID = "FZKSONWSON11EP2X3P5EP84X24THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-10-1EP_2x3mm_P0.5mm_EP0.84x2.4mm_ThermalVias', 'description': 'WSON-10 package 2x3mm body, pitch 0.5mm, thermal vias and counter-pad, see http://www.ti.com/lit/ds/symlink/tps62177.pdf', 'tags': 'WSON 0.5 thermal vias', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-10-1EP_2x3mm_Pitch0.5mm_EP0.84x2.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-10-1EP_2x3mm_P0.5mm_EP0.84x2.4mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

