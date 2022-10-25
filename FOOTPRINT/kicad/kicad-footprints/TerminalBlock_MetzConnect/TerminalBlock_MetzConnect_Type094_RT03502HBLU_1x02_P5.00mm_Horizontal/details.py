
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type094_RT03502HBLU_1x02_P5.00mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE94RT352HBLU1X2P5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type094_RT03502HBLU_1x02_P5.00mm_Horizontal', 'description': 'terminal block Metz Connect Type094_RT03502HBLU, 2 pins, pitch 5mm, size 10x8.3mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.metz-connect.com/ru/system/files/productfiles/Data_sheet_310941_RT035xxHBLU_OFF-022742T.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type094_RT03502HBLU pitch 5mm size 10x8.3mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type094_RT03502HBLU_1x02_P5.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type094_RT03502HBLU_1x02_P5.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

