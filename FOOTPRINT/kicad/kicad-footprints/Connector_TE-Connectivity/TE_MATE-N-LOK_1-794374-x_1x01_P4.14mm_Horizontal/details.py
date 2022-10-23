
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_TE-Connectivity"
    oIndex = "TE_MATE-N-LOK_1-794374-x_1x01_P4.14mm_Horizontal"
    hexID = "FZKCNTECONNECTIVITYTEMATENLOK1794374X1X1P414HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_MATE-N-LOK_1-794374-x_1x01_P4.14mm_Horizontal', 'description': 'Molex Mini-Universal MATE-N-LOK, old mpn/engineering number: 1-794374-x, 1 Pins per row (http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=82181_SOFTSHELL_HIGH_DENSITY&DocType=CS&DocLang=EN), generated with kicad-footprint-generator', 'tags': 'connector TE MATE-N-LOK top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_TE-Connectivity.3dshapes/TE_MATE-N-LOK_1-794374-x_1x01_P4.14mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_TE-Connectivity : TE_MATE-N-LOK_1-794374-x_1x01_P4.14mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

