
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_SUR_SM16B-SURS-TF_1x16-1MP_P0.80mm_Horizontal"
    hexID = "FZKCNJSTJSTSURSM16BSURSTF1X161MPP8HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_SUR_SM16B-SURS-TF_1x16-1MP_P0.80mm_Horizontal', 'description': 'JST SUR series connector, SM16B-SURS-TF (http://www.jst-mfg.com/product/pdf/eng/eSUR.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST SUR top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_SUR_SM16B-SURS-TF_1x16-1MP_P0.80mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_SUR_SM16B-SURS-TF_1x16-1MP_P0.80mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

