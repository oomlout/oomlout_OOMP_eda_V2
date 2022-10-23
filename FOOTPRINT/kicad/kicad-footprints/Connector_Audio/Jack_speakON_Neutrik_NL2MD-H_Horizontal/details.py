
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_speakON_Neutrik_NL2MD-H_Horizontal"
    hexID = "FZKCNAUDIOJSPEAKONNEUTRIKNL2MDHHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_speakON_Neutrik_NL2MD-H_Horizontal', 'description': 'speakON Chassis Connectors, 2 pole chassis connector, gray D-size flange, countersunk thru holes, horizontal PCB, https://www.neutrik.com/en/product/nl2md-h', 'tags': 'neutrik speakon', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NL2MD-H_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_speakON_Neutrik_NL2MD-H_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

