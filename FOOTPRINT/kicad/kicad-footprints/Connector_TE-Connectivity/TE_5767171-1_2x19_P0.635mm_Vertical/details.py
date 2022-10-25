
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_TE-Connectivity"
    oIndex = "TE_5767171-1_2x19_P0.635mm_Vertical"
    hexID = "FZKCNTECONNECTIVITYTE576717112X19P635VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_5767171-1_2x19_P0.635mm_Vertical', 'description': 'PCB Mount Receptacle, Vertical, Board-to-Board, 38 Position, 24.003mm / .64mm [.945in] Centerline, Header Only, Palladium Nickel (https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F5767171%7FB2%7Fpdf%7FEnglish%7FENG_CD_5767171_B2.pdf%7F5767171-1#page=2)', 'tags': 'mictor38 receptacle board-to-board', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_TE-Connectivity.3dshapes/TE_5767171-1_2x19_P0.635mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_TE-Connectivity : TE_5767171-1_2x19_P0.635mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

