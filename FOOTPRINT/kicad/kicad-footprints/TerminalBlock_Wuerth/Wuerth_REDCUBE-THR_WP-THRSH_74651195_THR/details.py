
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Wuerth"
    oIndex = "Wuerth_REDCUBE-THR_WP-THRSH_74651195_THR"
    hexID = "FZKTBWUERTHWUERTHREDCUBETHRWPTHRSH74651195THR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wuerth_REDCUBE-THR_WP-THRSH_74651195_THR', 'description': 'REDCUBE THR with internal through-hole thread WP-THRSH (https://www.we-online.de/katalog/datasheet/74651195.pdf)', 'tags': 'screw terminal thread redcube thr power connector', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Wuerth.3dshapes/Wuerth_REDCUBE-THR_WP-THRSH_74651195_THR.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('TerminalBlock_Wuerth : Wuerth_REDCUBE-THR_WP-THRSH_74651195_THR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

