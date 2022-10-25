
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type205_RT04502UBLC_1x02_P5.00mm_45Degree"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE25RT452UBLC1X2P545DEGREE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type205_RT04502UBLC_1x02_P5.00mm_45Degree', 'description': 'terminal block Metz Connect Type205_RT04502UBLC, 45Degree (cable under 45degree), 2 pins, pitch 5mm, size 10x12.5mm^2, drill diamater 1.4mm, pad diameter 2.7mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_312051_RT045xxUBLC_OFF-022759T.pdf, script-generated with , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type205_RT04502UBLC 45Degree pitch 5mm size 10x12.5mm^2 drill 1.4mm pad 2.7mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type205_RT04502UBLC_1x02_P5.00mm_45Degree.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type205_RT04502UBLC_1x02_P5.00mm_45Degree')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

