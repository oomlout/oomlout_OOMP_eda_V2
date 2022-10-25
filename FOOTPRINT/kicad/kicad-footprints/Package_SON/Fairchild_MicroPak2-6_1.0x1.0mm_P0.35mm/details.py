
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Fairchild_MicroPak2-6_1.0x1.0mm_P0.35mm"
    hexID = "FZKSONFAIRCHILDMPAK261X1P35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fairchild_MicroPak2-6_1.0x1.0mm_P0.35mm', 'description': 'Fairchild-specific MicroPak2-6 1.0x1.0mm Pitch 0.35mm https://www.nxp.com/docs/en/application-note/AN10343.pdff', 'tags': 'Fairchild-specific MicroPak2-6 1.0x1.0mm Pitch 0.35mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Fairchild_MicroPak2-6_1.0x1.0mm_P0.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Fairchild_MicroPak2-6_1.0x1.0mm_P0.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

