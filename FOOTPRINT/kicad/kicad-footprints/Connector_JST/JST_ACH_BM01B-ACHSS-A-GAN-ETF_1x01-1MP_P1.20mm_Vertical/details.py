
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_ACH_BM01B-ACHSS-A-GAN-ETF_1x01-1MP_P1.20mm_Vertical"
    hexID = "FZKCNJSTJSTACHBM1BACHSSAGANETF1X11MPP12VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_ACH_BM01B-ACHSS-A-GAN-ETF_1x01-1MP_P1.20mm_Vertical', 'description': 'JST ACH series connector, BM01B-ACHSS-A-GAN-ETF (http://www.jst-mfg.com/product/pdf/eng/eACH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST ACH vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_ACH_BM01B-ACHSS-A-GAN-ETF_1x01-1MP_P1.20mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_ACH_BM01B-ACHSS-A-GAN-ETF_1x01-1MP_P1.20mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

