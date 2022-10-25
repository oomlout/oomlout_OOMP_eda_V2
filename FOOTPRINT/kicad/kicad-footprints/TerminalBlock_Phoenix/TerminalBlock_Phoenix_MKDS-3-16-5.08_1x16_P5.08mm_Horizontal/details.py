
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_MKDS-3-16-5.08_1x16_P5.08mm_Horizontal"
    hexID = "FZKTBPHOENIXTBPHOENIXMKDS316581X16P58HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_MKDS-3-16-5.08_1x16_P5.08mm_Horizontal', 'description': 'Terminal Block Phoenix MKDS-3-16-5.08, 16 pins, pitch 5.08mm, size 81.3x11.2mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.farnell.com/datasheets/2138224.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix', 'tags': 'THT Terminal Block Phoenix MKDS-3-16-5.08 pitch 5.08mm size 81.3x11.2mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_MKDS-3-16-5.08_1x16_P5.08mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_MKDS-3-16-5.08_1x16_P5.08mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

