
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_Type703_RT10N03HGLU_1x03_P9.52mm_Horizontal"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECTTYPE73RT1N3HGLU1X3P952HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_Type703_RT10N03HGLU_1x03_P9.52mm_Horizontal', 'description': 'terminal block Metz Connect Type703_RT10N03HGLU, 3 pins, pitch 9.52mm, size 28.6x12.5mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.metz-connect.com/de/system/files/productfiles/Datenblatt_317031_RT10NxxHGLU_OFF-022897S.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT terminal block Metz Connect Type703_RT10N03HGLU pitch 9.52mm size 28.6x12.5mm^2 drill 1.3mm pad 2.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_Type703_RT10N03HGLU_1x03_P9.52mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_Type703_RT10N03HGLU_1x03_P9.52mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

