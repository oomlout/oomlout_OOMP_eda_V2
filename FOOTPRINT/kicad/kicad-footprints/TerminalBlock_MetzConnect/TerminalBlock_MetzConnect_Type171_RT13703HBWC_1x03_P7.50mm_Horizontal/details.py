
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type171_RT13703HBWC_1x03_P7.50mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE171RT1373HBWC1X3P75HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type171_RT13703HBWC_1x03_P7.50mm_Horizontal', 'description': 'terminal block Metz Connect Type171_RT13703HBWC, 3 pins, pitch 7.5mm, size 22.5x9mm^2, drill diamater 1.3mm, pad diameter 2.5mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_311711_RT137xxHBWC_OFF-022811Q.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type171_RT13703HBWC pitch 7.5mm size 22.5x9mm^2 drill 1.3mm pad 2.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type171_RT13703HBWC_1x03_P7.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type171_RT13703HBWC_1x03_P7.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

