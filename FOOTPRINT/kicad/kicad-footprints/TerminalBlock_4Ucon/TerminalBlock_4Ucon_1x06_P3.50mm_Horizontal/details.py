
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_4Ucon"
    oIndex = "TerminalBlock_4Ucon_1x06_P3.50mm_Horizontal"
    hexID = "FZKTB4UCONTB4UCON1X6P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_4Ucon_1x06_P3.50mm_Horizontal', 'description': 'Terminal Block 4Ucon ItemNo. 19964, 6 pins, pitch 3.5mm, size 21.7x7mm^2, drill diamater 1.2mm, pad diameter 2.4mm, see http://www.4uconnector.com/online/object/4udrawing/19964.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_4Ucon', 'tags': 'THT Terminal Block 4Ucon ItemNo. 19964 pitch 3.5mm size 21.7x7mm^2 drill 1.2mm pad 2.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_4Ucon.3dshapes/TerminalBlock_4Ucon_1x06_P3.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_4Ucon : TerminalBlock_4Ucon_1x06_P3.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

