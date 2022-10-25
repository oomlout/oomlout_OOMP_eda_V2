
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_PT-1,5-8-5.0-H_1x08_P5.00mm_Horizontal"
    hexID = "FZKTBPHOENIXTBPHOENIXPT1585H1X8P5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_PT-1,5-8-5.0-H_1x08_P5.00mm_Horizontal', 'description': 'Terminal Block Phoenix PT-1,5-8-5.0-H, 8 pins, pitch 5mm, size 40x9mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.mouser.com/ds/2/324/ItemDetail_1935161-922578.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix', 'tags': 'THT Terminal Block Phoenix PT-1,5-8-5.0-H pitch 5mm size 40x9mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_PT-1,5-8-5.0-H_1x08_P5.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_PT-1,5-8-5.0-H_1x08_P5.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

