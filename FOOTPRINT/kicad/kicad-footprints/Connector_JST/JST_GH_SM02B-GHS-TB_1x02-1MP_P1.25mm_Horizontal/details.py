
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_GH_SM02B-GHS-TB_1x02-1MP_P1.25mm_Horizontal"
    hexID = "FZKCNJSTJSTGHSM2BGHSTB1X21MPP125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_GH_SM02B-GHS-TB_1x02-1MP_P1.25mm_Horizontal', 'description': 'JST GH series connector, SM02B-GHS-TB (http://www.jst-mfg.com/product/pdf/eng/eGH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST GH top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_GH_SM02B-GHS-TB_1x02-1MP_P1.25mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_GH_SM02B-GHS-TB_1x02-1MP_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

