
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-JSTSH-X-PI09-SM-HSH9"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADJSTSHXPI9SMHSH9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HEAD-JSTSH-X-PI09-SM-HSH9', 'description': 'hexID: HSH9; JST SH series connector, BM09B-SRSS-TB (http://www.jst-mfg.com/product/pdf/eng/eSH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST SH side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_SH_BM09B-SRSS-TB_1x09-1MP_P1.00mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_parts : HEAD-JSTSH-X-PI09-SM-HSH9')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

