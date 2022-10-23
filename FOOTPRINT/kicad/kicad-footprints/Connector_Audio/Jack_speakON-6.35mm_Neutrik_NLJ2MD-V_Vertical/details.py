
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_speakON-6.35mm_Neutrik_NLJ2MD-V_Vertical"
    hexID = "FZKCNAUDIOJSPEAKON635NEUTRIKNLJ2MDVVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_speakON-6.35mm_Neutrik_NLJ2MD-V_Vertical', 'description': 'speakON Combo, 2 pole combination of speakON socket and 6.35mm (1/4in) jack receptacle, vertical pcb mount, https://www.neutrik.com/en/product/nlj2md-v', 'tags': 'neutrik speakon combo', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON-6.35mm_Neutrik_NLJ2MD-V_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_speakON-6.35mm_Neutrik_NLJ2MD-V_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

