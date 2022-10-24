
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-56_3.170x3.444mm_Layout7x8_P0.4mm"
    hexID = "FZKCSPWLCSP56317X3444LAYOUT7X8P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-56_3.170x3.444mm_Layout7x8_P0.4mm', 'description': 'WLCSP-56, 7x8 raster, 3.170x3.444mm package, pitch 0.4mm; see section 48.2.4 of http://ww1.microchip.com/downloads/en/DeviceDoc/DS60001479B.pdf', 'tags': 'BGA 56 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-56_3.170x3.444mm_Layout7x8_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-56_3.170x3.444mm_Layout7x8_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

