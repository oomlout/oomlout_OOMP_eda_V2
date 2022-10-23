
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_PH_S10B-PH-SM4-TB_1x10-1MP_P2.00mm_Horizontal"
    hexID = "FZKCNJSTJSTPHS1BPHSM4TB1X11MPP2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_PH_S10B-PH-SM4-TB_1x10-1MP_P2.00mm_Horizontal', 'description': 'JST PH series connector, S10B-PH-SM4-TB (http://www.jst-mfg.com/product/pdf/eng/ePH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST PH top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_PH_S10B-PH-SM4-TB_1x10-1MP_P2.00mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_PH_S10B-PH-SM4-TB_1x10-1MP_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

