
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Infineon_LFBGA-292_17x17mm_Layout20x20_P0.8mm_Ball0.5mm_Pad0.35"
    hexID = "FZKBGAINFINEONLFBGA29217X17LAYOUT2X2P8BALL5PAD35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_LFBGA-292_17x17mm_Layout20x20_P0.8mm_Ball0.5mm_Pad0.35', 'description': 'Infineon LFBGA-292, 0.35mm pad, 17.0x17.0mm, 292 Ball, 20x20 Layout, 0.8mm Pitch, https://www.infineon.com/cms/en/product/packages/PG-LFBGA/PG-LFBGA-292-11/', 'tags': 'BGA 292 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Infineon_LFBGA-292_17x17mm_Layout20x20_P0.8mm_Ball0.5mm_Pad0.35.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Infineon_LFBGA-292_17x17mm_Layout20x20_P0.8mm_Ball0.5mm_Pad0.35')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

