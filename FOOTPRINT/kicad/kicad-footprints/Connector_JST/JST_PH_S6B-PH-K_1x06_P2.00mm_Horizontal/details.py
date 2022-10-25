
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_PH_S6B-PH-K_1x06_P2.00mm_Horizontal"
    hexID = "FZKCNJSTJSTPHS6BPHK1X6P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_PH_S6B-PH-K_1x06_P2.00mm_Horizontal', 'description': 'JST PH series connector, S6B-PH-K (http://www.jst-mfg.com/product/pdf/eng/ePH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST PH top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_PH_S6B-PH-K_1x06_P2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_PH_S6B-PH-K_1x06_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

