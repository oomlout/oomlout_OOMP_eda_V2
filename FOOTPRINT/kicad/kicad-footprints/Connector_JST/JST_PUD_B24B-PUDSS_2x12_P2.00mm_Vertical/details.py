
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_PUD_B24B-PUDSS_2x12_P2.00mm_Vertical"
    hexID = "FZKCNJSTJSTPUDB24BPUDSS2X12P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_PUD_B24B-PUDSS_2x12_P2.00mm_Vertical', 'description': 'JST PUD series connector, B24B-PUDSS (http://www.jst-mfg.com/product/pdf/eng/ePUD.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST PUD side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_PUD_B24B-PUDSS_2x12_P2.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_PUD_B24B-PUDSS_2x12_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

