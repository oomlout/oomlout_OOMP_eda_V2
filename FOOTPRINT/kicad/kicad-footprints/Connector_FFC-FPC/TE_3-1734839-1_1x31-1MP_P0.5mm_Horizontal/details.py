
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "TE_3-1734839-1_1x31-1MP_P0.5mm_Horizontal"
    hexID = "FZKCNFFCFPCTE3173483911X311MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_3-1734839-1_1x31-1MP_P0.5mm_Horizontal', 'description': 'TE FPC connector, 31 top-side contacts, 0.5mm pitch, SMT, https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F1734839%7FC%7Fpdf%7FEnglish%7FENG_CD_1734839_C_C_1734839.pdf%7F4-1734839-0', 'tags': 'te fpc 1734839', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/TE_3-1734839-1_1x31-1MP_P0.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : TE_3-1734839-1_1x31-1MP_P0.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

