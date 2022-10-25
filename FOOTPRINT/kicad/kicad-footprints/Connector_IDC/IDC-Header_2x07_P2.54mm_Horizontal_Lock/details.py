
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_IDC"
    oIndex = "IDC-Header_2x07_P2.54mm_Horizontal_Lock"
    hexID = "FZKCNIDCIDCHEADER2X7P254HORIZONTALL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'IDC-Header_2x07_P2.54mm_Horizontal_Lock', 'description': 'Connector IDC Locked, 10 contacts, compatible header: PANCON HE10 (Series 50, (https://www.reboul.fr/storage/00003af6.pdf)', 'tags': 'connector idc locked', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_IDC.3dshapes/IDC-Header_2x07_P2.54mm_Horizontal_Lock.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_IDC : IDC-Header_2x07_P2.54mm_Horizontal_Lock')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

