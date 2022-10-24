
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_PTSM-0,5-4-2.5-H-THR_1x04_P2.50mm_Horizontal"
    hexID = "FZKTBPHOENIXTBPHOENIXPTSM5425HTHR1X4P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_PTSM-0,5-4-2.5-H-THR_1x04_P2.50mm_Horizontal', 'description': 'Terminal Block Phoenix PTSM-0,5-4-2.5-H-THR, 4 pins, pitch 2.5mm, size 12.2x10mm^2, drill diamater 1.2mm, pad diameter 3mm, see http://www.produktinfo.conrad.com/datenblaetter/550000-574999/556441-da-01-de-LEITERPLATTENKL__PTSM_0_5__8_2_5_H_THR.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix', 'tags': 'THT Terminal Block Phoenix PTSM-0,5-4-2.5-H-THR pitch 2.5mm size 12.2x10mm^2 drill 1.2mm pad 3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_PTSM-0,5-4-2.5-H-THR_1x04_P2.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_PTSM-0,5-4-2.5-H-THR_1x04_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

