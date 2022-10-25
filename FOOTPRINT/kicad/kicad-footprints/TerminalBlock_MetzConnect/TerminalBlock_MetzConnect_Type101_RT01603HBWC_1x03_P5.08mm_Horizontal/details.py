
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type101_RT01603HBWC_1x03_P5.08mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE11RT163HBWC1X3P58HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type101_RT01603HBWC_1x03_P5.08mm_Horizontal', 'description': 'terminal block Metz Connect Type101_RT01603HBWC, 3 pins, pitch 5.08mm, size 15.2x8mm^2, drill diamater 1.3mm, pad diameter 2.5mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_311011_RT016xxHBWC_OFF-022771S.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type101_RT01603HBWC pitch 5.08mm size 15.2x8mm^2 drill 1.3mm pad 2.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type101_RT01603HBWC_1x03_P5.08mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type101_RT01603HBWC_1x03_P5.08mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

