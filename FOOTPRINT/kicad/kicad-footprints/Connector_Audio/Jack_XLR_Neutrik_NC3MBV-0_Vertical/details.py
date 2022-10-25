
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR_Neutrik_NC3MBV-0_Vertical"
    hexID = "FZKCNAUDIOJXLRNEUTRIKNC3MBVVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR_Neutrik_NC3MBV-0_Vertical', 'description': 'B Series, 3 pole male XLR receptacle, grounding: ground contact connected to shell ground, but not to front panel and Pin 1, steel retention lug, vertical PCB mount, https://www.neutrik.com/en/product/nc3mbv-0', 'tags': 'neutrik xlr b', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3MBV-0_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR_Neutrik_NC3MBV-0_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

