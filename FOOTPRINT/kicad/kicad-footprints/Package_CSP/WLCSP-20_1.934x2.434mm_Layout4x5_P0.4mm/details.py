
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-20_1.934x2.434mm_Layout4x5_P0.4mm"
    hexID = "FZKCSPWLCSP21934X2434LAYOUT4X5P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-20_1.934x2.434mm_Layout4x5_P0.4mm', 'description': 'WLCSP-20, 4x5 raster, 1.934x2.434mm package, pitch 0.4mm; see section 36.2.3 of http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42363-SAM-D11_Datasheet.pdf', 'tags': 'BGA 20 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-20_1.934x2.434mm_Layout4x5_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-20_1.934x2.434mm_Layout4x5_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

