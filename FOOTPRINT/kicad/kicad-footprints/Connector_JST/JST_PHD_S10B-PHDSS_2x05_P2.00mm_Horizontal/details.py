
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_PHD_S10B-PHDSS_2x05_P2.00mm_Horizontal"
    hexID = "FZKCNJSTJSTPHDS1BPHDSS2X5P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_PHD_S10B-PHDSS_2x05_P2.00mm_Horizontal', 'description': 'JST PHD series connector, S10B-PHDSS (http://www.jst-mfg.com/product/pdf/eng/ePHD.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST PHD horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_PHD_S10B-PHDSS_2x05_P2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_PHD_S10B-PHDSS_2x05_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

