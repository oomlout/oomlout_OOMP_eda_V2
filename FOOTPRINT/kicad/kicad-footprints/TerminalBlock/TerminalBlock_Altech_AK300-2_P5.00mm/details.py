
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock"
    oIndex = "TerminalBlock_Altech_AK300-2_P5.00mm"
    hexID = "FZKTBTBALTECHAK32P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Altech_AK300-2_P5.00mm', 'description': 'Altech AK300 terminal block, pitch 5.0mm, 45 degree angled, see http://www.mouser.com/ds/2/16/PCBMETRC-24178.pdf', 'tags': 'Altech AK300 terminal block pitch 5.0mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock.3dshapes/TerminalBlock_Altech_AK300-2_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock : TerminalBlock_Altech_AK300-2_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

