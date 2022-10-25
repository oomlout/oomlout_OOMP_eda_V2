
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_SH_BM02B-SRSS-TB_1x02-1MP_P1.00mm_Vertical"
    hexID = "FZKCNJSTJSTSHBM2BSRSSTB1X21MPP1VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_SH_BM02B-SRSS-TB_1x02-1MP_P1.00mm_Vertical', 'description': 'JST SH series connector, BM02B-SRSS-TB (http://www.jst-mfg.com/product/pdf/eng/eSH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST SH side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_SH_BM02B-SRSS-TB_1x02-1MP_P1.00mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_SH_BM02B-SRSS-TB_1x02-1MP_P1.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

