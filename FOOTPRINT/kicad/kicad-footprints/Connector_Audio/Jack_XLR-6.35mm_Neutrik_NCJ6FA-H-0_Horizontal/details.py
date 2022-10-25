
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR-6.35mm_Neutrik_NCJ6FA-H-0_Horizontal"
    hexID = "FZKCNAUDIOJXLR635NEUTRIKNCJ6FAHHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR-6.35mm_Neutrik_NCJ6FA-H-0_Horizontal', 'description': 'Combo A series, 3 pole XLR female receptacle with 6.35mm (1/4in) stereo jack, horizontal PCB mount, retention spring, https://www.neutrik.com/en/product/ncj6fa-h-0', 'tags': 'neutrik jack combo a', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR-6.35mm_Neutrik_NCJ6FA-H-0_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR-6.35mm_Neutrik_NCJ6FA-H-0_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

