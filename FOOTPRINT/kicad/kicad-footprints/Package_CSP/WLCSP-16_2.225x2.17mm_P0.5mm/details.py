
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-16_2.225x2.17mm_P0.5mm"
    hexID = "FZKCSPWLCSP162225X217P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-16_2.225x2.17mm_P0.5mm', 'description': 'WLCSP-16 2.225x2.17mm, 2.17x2.225mm, 16 Ball, 4x4 Layout, 0.5mm Pitch, https://ww1.microchip.com/downloads/en/DeviceDoc/16B_WLCSP_CS_C04-06036c.pdf', 'tags': 'CSP 16 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-16_2.225x2.17mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-16_2.225x2.17mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

