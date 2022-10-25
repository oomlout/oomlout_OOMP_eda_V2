
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_ZE_B08B-ZESK-1D_1x08_P1.50mm_Vertical"
    hexID = "FZKCNJSTJSTZEB8BZESK1D1X8P15VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_ZE_B08B-ZESK-1D_1x08_P1.50mm_Vertical', 'description': 'JST ZE series connector, B08B-ZESK-1D, with boss (http://www.jst-mfg.com/product/pdf/eng/eZE.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST ZE side entry boss', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_ZE_B08B-ZESK-1D_1x08_P1.50mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_ZE_B08B-ZESK-1D_1x08_P1.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

