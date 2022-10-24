
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type059_RT06303HBWC_1x03_P3.50mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE59RT633HBWC1X3P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type059_RT06303HBWC_1x03_P3.50mm_Horizontal', 'description': 'terminal block Metz Connect Type059_RT06303HBWC, 3 pins, pitch 3.5mm, size 10.5x6.5mm^2, drill diamater 1.2mm, pad diameter 2.3mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_310591_RT063xxHBWC_OFF-022684T.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type059_RT06303HBWC pitch 3.5mm size 10.5x6.5mm^2 drill 1.2mm pad 2.3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type059_RT06303HBWC_1x03_P3.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type059_RT06303HBWC_1x03_P3.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

