
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_IDC"
    oIndex = "IDC-Header_2x06-1MP_P2.54mm_Latch12.0mm_Vertical"
    hexID = "FZKCNIDCIDCHEADER2X61MPP254LATCH12VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'IDC-Header_2x06-1MP_P2.54mm_Latch12.0mm_Vertical', 'description': 'Through hole IDC header, 2x06, 2.54mm pitch, DIN 41651 / IEC 60603-13, double rows, 12.0mm latches, mounting holes, https://docs.google.com/spreadsheets/d/16SsEcesNF15N3Lb4niX7dcUr-NY5_MFPQhobNuNppn4/edit#gid=0', 'tags': 'Through hole vertical IDC header THT 2x06 2.54mm double row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_IDC.3dshapes/IDC-Header_2x06-1MP_P2.54mm_Latch12.0mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_IDC : IDC-Header_2x06-1MP_P2.54mm_Latch12.0mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

