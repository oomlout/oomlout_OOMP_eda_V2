
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_speakON_Neutrik_NL4MD-V-R_Vertical"
    hexID = "FZKCNAUDIOJSPEAKONNEUTRIKNL4MDVRVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_speakON_Neutrik_NL4MD-V-R_Vertical', 'description': 'speakON Chassis Connectors, 4 pole chassis connector, red D-size flange, countersunk thru holes, vertical PCB mount, https://www.neutrik.com/en/product/nl4md-v-r', 'tags': 'neutrik speakon', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NL4MD-V-R_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_speakON_Neutrik_NL4MD-V-R_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

