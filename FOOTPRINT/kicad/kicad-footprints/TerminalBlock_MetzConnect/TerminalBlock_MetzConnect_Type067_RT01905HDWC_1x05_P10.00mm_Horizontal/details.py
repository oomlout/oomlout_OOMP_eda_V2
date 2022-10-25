
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type067_RT01905HDWC_1x05_P10.00mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE67RT195HDWC1X5P1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type067_RT01905HDWC_1x05_P10.00mm_Horizontal', 'description': 'terminal block Metz Connect Type067_RT01905HDWC, 5 pins, pitch 10mm, size 45.8x8.2mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_310671_RT019xxHDWC_OFF-023605N.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type067_RT01905HDWC pitch 10mm size 45.8x8.2mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type067_RT01905HDWC_1x05_P10.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type067_RT01905HDWC_1x05_P10.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

