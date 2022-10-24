
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Wuerth"
    oIndex = "Wuerth_REDCUBE-THR_WP-THRBU_74650195_THR"
    hexID = "FZKTBWUERTHWUERTHREDCUBETHRWPTHRBU7465195THR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wuerth_REDCUBE-THR_WP-THRBU_74650195_THR', 'description': 'REDCUBE THR with internal through-hole thread WP-THRBU (https://www.we-online.de/katalog/datasheet/74650195.pdf)', 'tags': 'screw terminal thread redcube thr power connector', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Wuerth.3dshapes/Wuerth_REDCUBE-THR_WP-THRBU_74650195_THR.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('TerminalBlock_Wuerth : Wuerth_REDCUBE-THR_WP-THRBU_74650195_THR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

