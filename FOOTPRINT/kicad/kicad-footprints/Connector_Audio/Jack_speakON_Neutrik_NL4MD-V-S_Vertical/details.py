
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_speakON_Neutrik_NL4MD-V-S_Vertical"
    hexID = "FZKCNAUDIOJSPEAKONNEUTRIKNL4MDVSVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_speakON_Neutrik_NL4MD-V-S_Vertical', 'description': 'speakON Chassis Connectors, 4 pole chassis connector, black D-size flange, switchable version of NL4MD-V with 8 vertical PCB contacts (4 switching contacts), https://www.neutrik.com/en/product/nl4md-v-s', 'tags': 'neutrik speakon', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NL4MD-V-S_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_speakON_Neutrik_NL4MD-V-S_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

