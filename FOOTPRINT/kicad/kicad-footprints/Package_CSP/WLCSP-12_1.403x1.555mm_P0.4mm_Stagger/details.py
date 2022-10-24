
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-12_1.403x1.555mm_P0.4mm_Stagger"
    hexID = "FZKCSPWLCSP12143X1555P4STAGGER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-12_1.403x1.555mm_P0.4mm_Stagger', 'description': 'WLCSP-12, 6x4 raster staggered array, 1.403x1.555mm package, pitch 0.4mm; http://ww1.microchip.com/downloads/en/devicedoc/atmel-8235-8-bit-avr-microcontroller-attiny20_datasheet.pdf#page=208', 'tags': 'CSP 12 0.2x0.346333', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-12_1.403x1.555mm_P0.4mm_Stagger.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-12_1.403x1.555mm_P0.4mm_Stagger')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

