
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_XA_S13B-XASK-1_1x13_P2.50mm_Horizontal"
    hexID = "FZKCNJSTJSTXAS13BXASK11X13P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_XA_S13B-XASK-1_1x13_P2.50mm_Horizontal', 'description': 'JST XA series connector, S13B-XASK-1 (http://www.jst-mfg.com/product/pdf/eng/eXA1.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST XA horizontal hook', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_XA_S13B-XASK-1_1x13_P2.50mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Connector_JST : JST_XA_S13B-XASK-1_1x13_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

