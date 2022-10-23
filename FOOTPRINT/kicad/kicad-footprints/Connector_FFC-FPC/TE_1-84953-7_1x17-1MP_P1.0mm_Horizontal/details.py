
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "TE_1-84953-7_1x17-1MP_P1.0mm_Horizontal"
    hexID = "FZKCNFFCFPCTE18495371X171MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_1-84953-7_1x17-1MP_P1.0mm_Horizontal', 'description': 'TE FPC connector, 17 top-side contacts, 1.0mm pitch, 1.0mm height, SMT, http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=84953&DocType=Customer+Drawing&DocLang=English&DocFormat=pdf&PartCntxt=84953-4', 'tags': 'te fpc 84953', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/TE_1-84953-7_1x17-1MP_P1.0mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : TE_1-84953-7_1x17-1MP_P1.0mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

