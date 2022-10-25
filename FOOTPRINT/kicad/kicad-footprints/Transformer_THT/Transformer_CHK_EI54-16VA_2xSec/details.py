
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_CHK_EI54-16VA_2xSec"
    hexID = "FZKTRTRCHKEI5416VA2XSEC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_CHK_EI54-16VA_2xSec', 'description': 'Trafo, Printtrafo, CHK, EI54, 16VA, 2x Sec,http://www.eratransformers.com/product-detail/19', 'tags': 'Trafo Printtrafo CHK EI54 16VA 2x Sec ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_CHK_EI54-16VA_2xSec.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_CHK_EI54-16VA_2xSec')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

