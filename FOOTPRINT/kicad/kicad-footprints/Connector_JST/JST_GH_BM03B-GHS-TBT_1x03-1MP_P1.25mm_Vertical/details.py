
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_GH_BM03B-GHS-TBT_1x03-1MP_P1.25mm_Vertical"
    hexID = "FZKCNJSTJSTGHBM3BGHSTBT1X31MPP125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_GH_BM03B-GHS-TBT_1x03-1MP_P1.25mm_Vertical', 'description': 'JST GH series connector, BM03B-GHS-TBT (http://www.jst-mfg.com/product/pdf/eng/eGH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST GH side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_GH_BM03B-GHS-TBT_1x03-1MP_P1.25mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_GH_BM03B-GHS-TBT_1x03-1MP_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

