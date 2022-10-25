
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_XAG_SM05B-XAGKS-BN-TB_1x05-1MP_P2.50mm_Horizontal"
    hexID = "FZKCNJSTJSTXAGSM5BXAGKSBNTB1X51MPP25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_XAG_SM05B-XAGKS-BN-TB_1x05-1MP_P2.50mm_Horizontal', 'description': 'JST XAG series connector, SM05B-XAGKS-BN-TB (http://www.jst-mfg.com/product/pdf/eng/eXAG.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST XAG top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_XAG_SM05B-XAGKS-BN-TB_1x05-1MP_P2.50mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_XAG_SM05B-XAGKS-BN-TB_1x05-1MP_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

