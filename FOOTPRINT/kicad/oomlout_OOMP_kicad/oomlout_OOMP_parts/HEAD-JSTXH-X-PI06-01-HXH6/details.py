
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-JSTXH-X-PI06-01-HXH6"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADJSTXHXPI61HXH6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HEAD-JSTXH-X-PI06-01-HXH6', 'description': 'hexID: HXH6; JST XH series connector, B6B-XH-AM, with boss (http://www.jst-mfg.com/product/pdf/eng/eXH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST XH vertical boss', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_XH_B6B-XH-AM_1x06_P2.50mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('oomlout_OOMP_parts : HEAD-JSTXH-X-PI06-01-HXH6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

