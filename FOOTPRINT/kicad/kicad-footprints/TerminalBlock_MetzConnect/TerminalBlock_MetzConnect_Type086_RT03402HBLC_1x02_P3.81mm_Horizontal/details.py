
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type086_RT03402HBLC_1x02_P3.81mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE86RT342HBLC1X2P381HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type086_RT03402HBLC_1x02_P3.81mm_Horizontal', 'description': 'terminal block Metz Connect Type086_RT03402HBLC, 2 pins, pitch 3.81mm, size 7.51x7.3mm^2, drill diamater 0.7mm, pad diameter 1.4mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_310861_RT034xxHBLC_OFF-026114K.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type086_RT03402HBLC pitch 3.81mm size 7.51x7.3mm^2 drill 0.7mm pad 1.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type086_RT03402HBLC_1x02_P3.81mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type086_RT03402HBLC_1x02_P3.81mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

