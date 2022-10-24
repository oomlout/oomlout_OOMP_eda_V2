
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock"
    oIndex = "TerminalBlock_Wuerth_691311400102_P7.62mm"
    hexID = "FZKTBTBWUERTH691311412P762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Wuerth_691311400102_P7.62mm', 'description': 'https://katalog.we-online.de/em/datasheet/6913114001xx.pdf', 'tags': 'Wuerth WR-TBL Series 3114 terminal block pitch 7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock.3dshapes/TerminalBlock_Wuerth_691311400102_P7.62mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock : TerminalBlock_Wuerth_691311400102_P7.62mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

