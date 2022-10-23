
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR_Neutrik_NC3MAFH-PH_Horizontal"
    hexID = "FZKCNAUDIOJXLRNEUTRIKNC3MAFHPHHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR_Neutrik_NC3MAFH-PH_Horizontal', 'description': 'A Series, Chassis connector H female (A series layout), mates with Phoenix MSTB2,5/3-ST, horizontal PCB mount, https://www.neutrik.com/en/product/nc3mafh-ph', 'tags': 'neutrik xlr a', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3MAFH-PH_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR_Neutrik_NC3MAFH-PH_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

