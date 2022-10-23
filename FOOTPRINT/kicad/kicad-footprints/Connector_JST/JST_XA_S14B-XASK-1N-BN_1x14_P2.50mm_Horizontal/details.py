
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_XA_S14B-XASK-1N-BN_1x14_P2.50mm_Horizontal"
    hexID = "FZKCNJSTJSTXAS14BXASK1NBN1X14P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_XA_S14B-XASK-1N-BN_1x14_P2.50mm_Horizontal', 'description': 'JST XA series connector, S14B-XASK-1N-BN (http://www.jst-mfg.com/product/pdf/eng/eXA1.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST XA horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_XA_S14B-XASK-1N-BN_1x14_P2.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_XA_S14B-XASK-1N-BN_1x14_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

