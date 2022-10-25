
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_SUR_BM08B-SURS-TF_1x08-1MP_P0.80mm_Vertical"
    hexID = "FZKCNJSTJSTSURBM8BSURSTF1X81MPP8VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_SUR_BM08B-SURS-TF_1x08-1MP_P0.80mm_Vertical', 'description': 'JST SUR series connector, BM08B-SURS-TF (http://www.jst-mfg.com/product/pdf/eng/eSUR.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST SUR side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_SUR_BM08B-SURS-TF_1x08-1MP_P0.80mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_SUR_BM08B-SURS-TF_1x08-1MP_P0.80mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

