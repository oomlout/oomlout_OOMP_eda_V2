
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_A_TE_292303-7_Horizontal"
    hexID = "FZKCNUUATE292337HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_A_TE_292303-7_Horizontal', 'description': 'USB type A, Horizontal, https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=292303&DocType=Customer+Drawing&DocLang=English', 'tags': 'USB_A Female Connector receptacle', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_A_TE_292303-7_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_A_TE_292303-7_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

