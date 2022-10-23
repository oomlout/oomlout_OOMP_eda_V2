
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_SHL_SM06B-SHLS-TF_1x06-1MP_P1.00mm_Horizontal"
    hexID = "FZKCNJSTJSTSHLSM6BSHLSTF1X61MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_SHL_SM06B-SHLS-TF_1x06-1MP_P1.00mm_Horizontal', 'description': 'JST SHL series connector, SM06B-SHLS-TF (http://www.jst-mfg.com/product/pdf/eng/eSHL.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST SHL top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_SHL_SM06B-SHLS-TF_1x06-1MP_P1.00mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_SHL_SM06B-SHLS-TF_1x06-1MP_P1.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

