
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_TE-Connectivity"
    oIndex = "TE_MATE-N-LOK_1-770858-x_2x05_P4.14mm_Vertical"
    hexID = "FZKCNTECONNECTIVITYTEMATENLOK177858X2X5P414VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_MATE-N-LOK_1-770858-x_2x05_P4.14mm_Vertical', 'description': 'Molex Mini-Universal MATE-N-LOK, old mpn/engineering number: 1-770858-x, 5 Pins per row (http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=82181_SOFTSHELL_HIGH_DENSITY&DocType=CS&DocLang=EN), generated with kicad-footprint-generator', 'tags': 'connector TE MATE-N-LOK side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_TE-Connectivity.3dshapes/TE_MATE-N-LOK_1-770858-x_2x05_P4.14mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_TE-Connectivity : TE_MATE-N-LOK_1-770858-x_2x05_P4.14mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

