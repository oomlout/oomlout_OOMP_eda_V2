
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_MKDS-1,5-12_1x12_P5.00mm_Horizontal"
    hexID = "FZKTBPHOENIXTBPHOENIXMKDS15121X12P5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_MKDS-1,5-12_1x12_P5.00mm_Horizontal', 'description': 'Terminal Block Phoenix MKDS-1,5-12, 12 pins, pitch 5mm, size 60x9.8mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.farnell.com/datasheets/100425.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix', 'tags': 'THT Terminal Block Phoenix MKDS-1,5-12 pitch 5mm size 60x9.8mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_MKDS-1,5-12_1x12_P5.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_MKDS-1,5-12_1x12_P5.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

