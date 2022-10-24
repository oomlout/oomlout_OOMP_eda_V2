
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Philmore"
    oIndex = "TerminalBlock_Philmore_TB133_1x03_P5.00mm_Horizontal"
    hexID = "FZKTBPHILMORETBPHILMORETB1331X3P5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Philmore_TB133_1x03_P5.00mm_Horizontal', 'description': 'Terminal Block Philmore , 3 pins, pitch 5mm, size 15x10.2mm^2, drill diamater 1.2mm, pad diameter 2.4mm, see http://www.philmore-datak.com/mc/Page%20197.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Philmore', 'tags': 'THT Terminal Block Philmore  pitch 5mm size 15x10.2mm^2 drill 1.2mm pad 2.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Philmore.3dshapes/TerminalBlock_Philmore_TB133_1x03_P5.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Philmore : TerminalBlock_Philmore_TB133_1x03_P5.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

