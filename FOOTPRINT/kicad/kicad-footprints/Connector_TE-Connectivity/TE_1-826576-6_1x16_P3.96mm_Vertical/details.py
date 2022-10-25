
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_TE-Connectivity"
    oIndex = "TE_1-826576-6_1x16_P3.96mm_Vertical"
    hexID = "FZKCNTECONNECTIVITYTE182657661X16P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_1-826576-6_1x16_P3.96mm_Vertical', 'description': 'TE, 1-826576-6, 16 Pins (https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=826576&DocType=Customer+Drawing&DocLang=English), generated with kicad-footprint-generator', 'tags': 'connector TE 826576 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_TE-Connectivity.3dshapes/TE_1-826576-6_1x16_P3.96mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_TE-Connectivity : TE_1-826576-6_1x16_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

