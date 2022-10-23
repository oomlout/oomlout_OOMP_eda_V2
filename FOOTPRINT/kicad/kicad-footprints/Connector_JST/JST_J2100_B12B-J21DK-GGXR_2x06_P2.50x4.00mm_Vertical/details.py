
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_J2100_B12B-J21DK-GGXR_2x06_P2.50x4.00mm_Vertical"
    hexID = "FZKCNJSTJSTJ21B12BJ21DKGGXR2X6P25X4VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_J2100_B12B-J21DK-GGXR_2x06_P2.50x4.00mm_Vertical', 'description': 'JST J2100 series connector, B12B-J21DK-GGXR (http://www.jst-mfg.com/product/pdf/eng/eJFA-J2000.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST J2100 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_J2100_B12B-J21DK-GGXR_2x06_P2.50x4.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_J2100_B12B-J21DK-GGXR_2x06_P2.50x4.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

