
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "TE_2-84952-1_1x21-1MP_P1.0mm_Horizontal"
    hexID = "FZKCNFFCFPCTE28495211X211MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_2-84952-1_1x21-1MP_P1.0mm_Horizontal', 'description': 'TE FPC connector, 21 bottom-side contacts, 1.0mm pitch, 1.0mm height, SMT, http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=84952&DocType=Customer+Drawing&DocLang=English&DocFormat=pdf&PartCntxt=84952-4', 'tags': 'te fpc 84952', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/TE_2-84952-1_1x21-1MP_P1.0mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : TE_2-84952-1_1x21-1MP_P1.0mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

