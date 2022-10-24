
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Micron_FBGA-78_9x10.5mm_Layout9x13_P0.8mm"
    hexID = "FZKBGAMNFBGA789X15LAYOUT9X13P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Micron_FBGA-78_9x10.5mm_Layout9x13_P0.8mm', 'description': 'FBGA-78, 10.5x9.0mm, 78 Ball, 9x13 Layout, 0.8mm Pitch, https://www.micron.com/-/media/client/global/documents/products/data-sheet/dram/ddr3/4gb_ddr3l.pdf#page=23', 'tags': 'BGA 78 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Micron_FBGA-78_9x10.5mm_Layout9x13_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Micron_FBGA-78_9x10.5mm_Layout9x13_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

