
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR_Neutrik_NC3FAAV2_Vertical"
    hexID = "FZKCNAUDIOJXLRNEUTRIKNC3FAAV2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR_Neutrik_NC3FAAV2_Vertical', 'description': 'AA Series, 3 pole female receptacle, grounding: separate ground contact to mating connector shell and front panel, vertical PCB mount, https://www.neutrik.com/en/product/nc3faav2', 'tags': 'neutrik xlr aa', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3FAAV2_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR_Neutrik_NC3FAAV2_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

