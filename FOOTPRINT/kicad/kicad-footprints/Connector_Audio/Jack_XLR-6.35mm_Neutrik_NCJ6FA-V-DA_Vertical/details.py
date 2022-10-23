
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR-6.35mm_Neutrik_NCJ6FA-V-DA_Vertical"
    hexID = "FZKCNAUDIOJXLR635NEUTRIKNCJ6FAVDAVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR-6.35mm_Neutrik_NCJ6FA-V-DA_Vertical', 'description': 'Combo A series, 3 pole XLR female receptacle with 6.35mm (1/4in) stereo jack, vertical PCB mount, asymmetric push, https://www.neutrik.com/en/product/ncj6fa-v-da', 'tags': 'neutrik jack combo a', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR-6.35mm_Neutrik_NCJ6FA-V-DA_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR-6.35mm_Neutrik_NCJ6FA-V-DA_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

