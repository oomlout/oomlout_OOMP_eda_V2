
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_XH_S12B-XH-A_1x12_P2.50mm_Horizontal"
    hexID = "FZKCNJSTJSTXHS12BXHA1X12P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_XH_S12B-XH-A_1x12_P2.50mm_Horizontal', 'description': 'JST XH series connector, S12B-XH-A (http://www.jst-mfg.com/product/pdf/eng/eXH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST XH top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_XH_S12B-XH-A_1x12_P2.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_XH_S12B-XH-A_1x12_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

