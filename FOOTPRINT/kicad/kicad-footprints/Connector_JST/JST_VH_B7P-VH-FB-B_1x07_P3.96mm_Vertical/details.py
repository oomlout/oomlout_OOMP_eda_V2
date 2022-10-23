
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_VH_B7P-VH-FB-B_1x07_P3.96mm_Vertical"
    hexID = "FZKCNJSTJSTVHB7PVHFBB1X7P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_VH_B7P-VH-FB-B_1x07_P3.96mm_Vertical', 'description': 'JST VH series connector, B7P-VH-FB-B, shrouded (http://www.jst-mfg.com/product/pdf/eng/eVH.pdf),  generated with kicad-footprint-generator', 'tags': 'connector JST VH side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_VH_B7P-VH-FB-B_1x07_P3.96mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_VH_B7P-VH-FB-B_1x07_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

