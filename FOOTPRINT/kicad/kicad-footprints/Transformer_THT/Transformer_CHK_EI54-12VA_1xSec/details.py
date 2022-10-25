
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_CHK_EI54-12VA_1xSec"
    hexID = "FZKTRTRCHKEI5412VA1XSEC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_CHK_EI54-12VA_1xSec', 'description': 'Trafo, Printtrafo, CHK, EI54, 12VA, 1x Sec,http://www.eratransformers.com/product-detail/19', 'tags': 'Trafo Printtrafo CHK EI54 12VA 1x Sec ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_CHK_EI54-12VA_1xSec.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_CHK_EI54-12VA_1xSec')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

