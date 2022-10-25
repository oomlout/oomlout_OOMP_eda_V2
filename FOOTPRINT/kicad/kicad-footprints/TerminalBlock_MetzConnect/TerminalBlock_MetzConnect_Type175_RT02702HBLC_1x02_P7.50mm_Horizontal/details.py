
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type175_RT02702HBLC_1x02_P7.50mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE175RT272HBLC1X2P75HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type175_RT02702HBLC_1x02_P7.50mm_Horizontal', 'description': 'terminal block Metz Connect Type175_RT02702HBLC, 2 pins, pitch 7.5mm, size 15x11mm^2, drill diamater 1.4mm, pad diameter 2.6mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_311751_RT027xxHBLC_OFF-022814U.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type175_RT02702HBLC pitch 7.5mm size 15x11mm^2 drill 1.4mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type175_RT02702HBLC_1x02_P7.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type175_RT02702HBLC_1x02_P7.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

