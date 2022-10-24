
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type073_RT02602HBLU_1x02_P5.08mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE73RT262HBLU1X2P58HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type073_RT02602HBLU_1x02_P5.08mm_Horizontal', 'description': 'terminal block Metz Connect Type073_RT02602HBLU, 2 pins, pitch 5.08mm, size 10.2x11mm^2, drill diamater 1.4mm, pad diameter 2.6mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_310731_RT026xxHBLU_OFF-022792U.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type073_RT02602HBLU pitch 5.08mm size 10.2x11mm^2 drill 1.4mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type073_RT02602HBLU_1x02_P5.08mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type073_RT02602HBLU_1x02_P5.08mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

