
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_PT-1,5-13-3.5-H_1x13_P3.50mm_Horizontal"
    hexID = "FZKTBPHOENIXTBPHOENIXPT151335H1X13P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_PT-1,5-13-3.5-H_1x13_P3.50mm_Horizontal', 'description': 'Terminal Block Phoenix PT-1,5-13-3.5-H, 13 pins, pitch 3.5mm, size 45.5x7.6mm^2, drill diamater 1.2mm, pad diameter 2.4mm, see , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix', 'tags': 'THT Terminal Block Phoenix PT-1,5-13-3.5-H pitch 3.5mm size 45.5x7.6mm^2 drill 1.2mm pad 2.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_PT-1,5-13-3.5-H_1x13_P3.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_PT-1,5-13-3.5-H_1x13_P3.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

