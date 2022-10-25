
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_VH_B5P-VH_1x05_P3.96mm_Vertical"
    hexID = "FZKCNJSTJSTVHB5PVH1X5P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_VH_B5P-VH_1x05_P3.96mm_Vertical', 'description': 'JST VH series connector, B5P-VH (http://www.jst-mfg.com/product/pdf/eng/eVH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST VH vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_VH_B5P-VH_1x05_P3.96mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_VH_B5P-VH_1x05_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

