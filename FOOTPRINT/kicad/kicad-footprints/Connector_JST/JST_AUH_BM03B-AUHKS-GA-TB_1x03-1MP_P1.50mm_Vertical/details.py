
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_AUH_BM03B-AUHKS-GA-TB_1x03-1MP_P1.50mm_Vertical"
    hexID = "FZKCNJSTJSTAUHBM3BAUHKSGATB1X31MPP15VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_AUH_BM03B-AUHKS-GA-TB_1x03-1MP_P1.50mm_Vertical', 'description': 'JST AUH series connector, BM03B-AUHKS-GA-TB (http://www.jst-mfg.com/product/pdf/eng/eAUH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST AUH side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_AUH_BM03B-AUHKS-GA-TB_1x03-1MP_P1.50mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_AUH_BM03B-AUHKS-GA-TB_1x03-1MP_P1.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

