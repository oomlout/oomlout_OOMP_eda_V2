
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_NV_B04P-NV_1x04_P5.00mm_Vertical"
    hexID = "FZKCNJSTJSTNVB4PNV1X4P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_NV_B04P-NV_1x04_P5.00mm_Vertical', 'description': 'JST NV series connector, B04P-NV (http://www.jst-mfg.com/product/pdf/eng/eNV.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST NV side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_NV_B04P-NV_1x04_P5.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_JST : JST_NV_B04P-NV_1x04_P5.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

