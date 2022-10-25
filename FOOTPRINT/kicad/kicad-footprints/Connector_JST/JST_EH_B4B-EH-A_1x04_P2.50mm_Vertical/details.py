
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_EH_B4B-EH-A_1x04_P2.50mm_Vertical"
    hexID = "FZKCNJSTJSTEHB4BEHA1X4P25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_EH_B4B-EH-A_1x04_P2.50mm_Vertical', 'description': 'JST EH series connector, B4B-EH-A (http://www.jst-mfg.com/product/pdf/eng/eEH.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST EH vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_EH_B4B-EH-A_1x04_P2.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JST : JST_EH_B4B-EH-A_1x04_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

