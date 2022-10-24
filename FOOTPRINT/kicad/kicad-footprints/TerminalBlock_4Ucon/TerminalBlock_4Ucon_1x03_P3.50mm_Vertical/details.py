
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_4Ucon"
    oIndex = "TerminalBlock_4Ucon_1x03_P3.50mm_Vertical"
    hexID = "FZKTB4UCONTB4UCON1X3P35VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_4Ucon_1x03_P3.50mm_Vertical', 'description': 'Terminal Block 4Ucon ItemNo. 10694, vertical (cable from top), 3 pins, pitch 3.5mm, size 11.5x8.3mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.4uconnector.com/online/object/4udrawing/10694.pdf, script-generated with , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_4Ucon', 'tags': 'THT Terminal Block 4Ucon ItemNo. 10694 vertical pitch 3.5mm size 11.5x8.3mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_4Ucon.3dshapes/TerminalBlock_4Ucon_1x03_P3.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_4Ucon : TerminalBlock_4Ucon_1x03_P3.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

