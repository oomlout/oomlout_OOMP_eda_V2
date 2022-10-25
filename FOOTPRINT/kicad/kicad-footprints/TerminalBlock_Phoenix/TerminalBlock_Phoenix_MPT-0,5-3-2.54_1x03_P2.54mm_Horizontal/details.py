
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_MPT-0,5-3-2.54_1x03_P2.54mm_Horizontal"
    hexID = "FZKTBPHOENIXTBPHOENIXMPT532541X3P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_MPT-0,5-3-2.54_1x03_P2.54mm_Horizontal', 'description': 'Terminal Block Phoenix MPT-0,5-3-2.54, 3 pins, pitch 2.54mm, size 8.08x6.2mm^2, drill diamater 1.1mm, pad diameter 2.2mm, see http://www.mouser.com/ds/2/324/ItemDetail_1725656-920552.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix', 'tags': 'THT Terminal Block Phoenix MPT-0,5-3-2.54 pitch 2.54mm size 8.08x6.2mm^2 drill 1.1mm pad 2.2mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_MPT-0,5-3-2.54_1x03_P2.54mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_MPT-0,5-3-2.54_1x03_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

