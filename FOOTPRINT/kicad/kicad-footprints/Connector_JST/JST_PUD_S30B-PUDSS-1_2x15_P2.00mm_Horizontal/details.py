
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_PUD_S30B-PUDSS-1_2x15_P2.00mm_Horizontal"
    hexID = "FZKCNJSTJSTPUDS3BPUDSS12X15P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_PUD_S30B-PUDSS-1_2x15_P2.00mm_Horizontal', 'description': 'JST PUD series connector, S30B-PUDSS-1 (http://www.jst-mfg.com/product/pdf/eng/ePUD.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST PUD top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_PUD_S30B-PUDSS-1_2x15_P2.00mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_PUD_S30B-PUDSS-1_2x15_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

