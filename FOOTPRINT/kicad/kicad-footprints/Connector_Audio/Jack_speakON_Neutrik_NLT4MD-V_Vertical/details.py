
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_speakON_Neutrik_NLT4MD-V_Vertical"
    hexID = "FZKCNAUDIOJSPEAKONNEUTRIKNLT4MDVVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_speakON_Neutrik_NLT4MD-V_Vertical', 'description': 'STX Series, 4 pole male chassis connector, metal housing, vertical PCB mount,  self tapping screw holes (A-screw), https://www.neutrik.com/en/product/nlt4md-v', 'tags': 'neutrik speakon stx', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NLT4MD-V_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_speakON_Neutrik_NLT4MD-V_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

