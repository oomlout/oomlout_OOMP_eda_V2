
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "TERS-35D-L-PI02-01-T35L2"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSTERS35DLPI21T35L2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TERS-35D-L-PI02-01-T35L2', 'description': 'hexID: T35L2; Terminal Block 4Ucon ItemNo. 10693, vertical (cable from top), 2 pins, pitch 3.5mm, size 8x8.3mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.4uconnector.com/online/object/4udrawing/10693.pdf, script-generated with , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_4Ucon', 'tags': 'THT Terminal Block 4Ucon ItemNo. 10693 vertical pitch 3.5mm size 8x8.3mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_4Ucon.3dshapes/TerminalBlock_4Ucon_1x02_P3.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('oomlout_OOMP_parts : TERS-35D-L-PI02-01-T35L2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

