
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Micron_FBGA-96_8x14mm_Layout9x16_P0.8mm"
    hexID = "FZKBGAMNFBGA968X14LAYOUT9X16P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Micron_FBGA-96_8x14mm_Layout9x16_P0.8mm', 'description': 'FBGA-96, 14.0x8.0mm, 96 Ball, 9x16 Layout, 0.8mm Pitch, https://www.micron.com/-/media/client/global/documents/products/data-sheet/dram/ddr3/4gb_ddr3l.pdf#page=28', 'tags': 'BGA 96 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Micron_FBGA-96_8x14mm_Layout9x16_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Micron_FBGA-96_8x14mm_Layout9x16_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

