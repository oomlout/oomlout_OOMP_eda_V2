
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm_ThermalVias"
    hexID = "FZKSONVSON11EP3X3P5EP165X24THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm_ThermalVias', 'description': 'VSON 10 Thermal on 11 3x3mm Pitch 0.5mm http://chip.tomsk.ru/chip/chipdoc.nsf/Package/D8A64DD165C2AAD9472579400024FC41!OpenDocument', 'tags': 'VSON 10 Thermal on 11 3x3mm Pitch 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

