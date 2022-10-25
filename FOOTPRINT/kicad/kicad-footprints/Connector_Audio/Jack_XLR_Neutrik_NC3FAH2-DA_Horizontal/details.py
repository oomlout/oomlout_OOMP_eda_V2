
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR_Neutrik_NC3FAH2-DA_Horizontal"
    hexID = "FZKCNAUDIOJXLRNEUTRIKNC3FAH2DAHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR_Neutrik_NC3FAH2-DA_Horizontal', 'description': 'A Series, 3 pole female XLR receptacle, grounding: separate ground contact to mating connector shell and front panel, horizontal PCB mount, asymmetric push, https://www.neutrik.com/en/product/nc3fah2-da', 'tags': 'neutrik xlr a', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3FAH2-DA_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR_Neutrik_NC3FAH2-DA_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

