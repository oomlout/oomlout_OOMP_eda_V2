
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_TE-Connectivity"
    oIndex = "TE_MATE-N-LOK_350211-1_1x04_P5.08mm_Vertical"
    hexID = "FZKCNTECONNECTIVITYTEMATENLOK3521111X4P58VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_MATE-N-LOK_350211-1_1x04_P5.08mm_Vertical', 'description': 'https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F350211%7FU5%7Fpdf%7FEnglish%7FENG_CD_350211_U5.pdf%7F350211-1', 'tags': 'connector TE MATE-N-LOK top entry ATA PATA IDE 5.25 inch floppy drive power', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_TE-Connectivity.3dshapes/TE_MATE-N-LOK_350211-1_1x04_P5.08mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_TE-Connectivity : TE_MATE-N-LOK_350211-1_1x04_P5.08mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

