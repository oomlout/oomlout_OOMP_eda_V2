
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X03-SHRO-H2X3SH"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X3SHROH2X3SH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HEAD-I01-X-PI2X03-SHRO-H2X3SH', 'description': 'hexID: H2X3SH; Through hole IDC box header, 2x03, 2.54mm pitch, DIN 41651 / IEC 60603-13, double rows, https://docs.google.com/spreadsheets/d/16SsEcesNF15N3Lb4niX7dcUr-NY5_MFPQhobNuNppn4/edit#gid=0', 'tags': 'Through hole vertical IDC box header THT 2x03 2.54mm double row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_IDC.3dshapes/IDC-Header_2x03_P2.54mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-X-PI2X03-SHRO-H2X3SH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

