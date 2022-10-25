
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_XA_B05B-XASK-1-A_1x05_P2.50mm_Vertical"
    hexID = "FZKCNJSTJSTXAB5BXASK1A1X5P25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_XA_B05B-XASK-1-A_1x05_P2.50mm_Vertical', 'description': 'JST XA series connector, B05B-XASK-1-A (http://www.jst-mfg.com/product/pdf/eng/eXA1.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST XA vertical boss', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_XA_B05B-XASK-1-A_1x05_P2.50mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_XA_B05B-XASK-1-A_1x05_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

