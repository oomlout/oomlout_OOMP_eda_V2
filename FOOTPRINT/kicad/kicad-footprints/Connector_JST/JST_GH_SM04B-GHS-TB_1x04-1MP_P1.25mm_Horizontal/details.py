
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal"
    hexID = "FZKCNJSTJSTGHSM4BGHSTB1X41MPP125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal', 'description': 'JST GH series connector, SM04B-GHS-TB (http://www.jst-mfg.com/product/pdf/eng/eGH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST GH top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

