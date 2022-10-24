
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Fairchild_MicroPak-6_1.0x1.45mm_P0.5mm"
    hexID = "FZKSONFAIRCHILDMPAK61X145P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fairchild_MicroPak-6_1.0x1.45mm_P0.5mm', 'description': 'Fairchild-specific MicroPak-6 1.0x1.45mm Pitch 0.5mm https://www.nxp.com/docs/en/application-note/AN10343.pdff', 'tags': 'Fairchild-specific MicroPak-6 1.0x1.45mm Pitch 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Fairchild_MicroPak-6_1.0x1.45mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Fairchild_MicroPak-6_1.0x1.45mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

