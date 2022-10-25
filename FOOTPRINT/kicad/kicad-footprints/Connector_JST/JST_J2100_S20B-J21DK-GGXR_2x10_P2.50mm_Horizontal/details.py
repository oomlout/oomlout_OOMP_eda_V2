
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_J2100_S20B-J21DK-GGXR_2x10_P2.50mm_Horizontal"
    hexID = "FZKCNJSTJSTJ21S2BJ21DKGGXR2X1P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_J2100_S20B-J21DK-GGXR_2x10_P2.50mm_Horizontal', 'description': 'JST J2100 series connector, S20B-J21DK-GGXR (http://www.jst-mfg.com/product/pdf/eng/eJFA-J2000.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST J2100 horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_J2100_S20B-J21DK-GGXR_2x10_P2.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_J2100_S20B-J21DK-GGXR_2x10_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

