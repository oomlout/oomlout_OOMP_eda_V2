
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR_Neutrik_NC3MBH-0_Horizontal"
    hexID = "FZKCNAUDIOJXLRNEUTRIKNC3MBHHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR_Neutrik_NC3MBH-0_Horizontal', 'description': 'B Series, 3 pole male XLR receptacle, grounding: ground contact connected to shell ground, but not to front panel and Pin 1, steel retention lug, horizontal PCB mount, https://www.neutrik.com/en/product/nc3mbh-0', 'tags': 'neutrik xlr b', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3MBH-0_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR_Neutrik_NC3MBH-0_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

