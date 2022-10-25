
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_SFH_SM02B-SFHRS-TF_1x02-1MP_P4.20mm_Horizontal"
    hexID = "FZKCNJSTJSTSFHSM2BSFHRSTF1X21MPP42HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_SFH_SM02B-SFHRS-TF_1x02-1MP_P4.20mm_Horizontal', 'description': 'JST SFH series connector, SM02B-SFHRS-TF (http://www.jst-mfg.com/product/pdf/eng/eSFH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST SFH horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_SFH_SM02B-SFHRS-TF_1x02-1MP_P4.20mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_SFH_SM02B-SFHRS-TF_1x02-1MP_P4.20mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

