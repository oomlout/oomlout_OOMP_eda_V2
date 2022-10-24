
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Microchip_TFBGA-196_11x11mm_Layout14x14_P0.75mm_SMD"
    hexID = "FZKBGAMCHIPTFBGA19611X11LAYOUT14X14P75SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Microchip_TFBGA-196_11x11mm_Layout14x14_P0.75mm_SMD', 'description': 'TFBGA-196, 11.0x11.0mm, 196 Ball, 14x14 Layout, 0.75mm Pitch, http://ww1.microchip.com/downloads/en/DeviceDoc/SAMA5D2-Series-Data-Sheet-DS60001476C.pdf#page=2956', 'tags': 'BGA 196 0.75', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Microchip_TFBGA-196_11x11mm_Layout14x14_P0.75mm_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Microchip_TFBGA-196_11x11mm_Layout14x14_P0.75mm_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

