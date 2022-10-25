
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_NF_ETAL_P3356"
    hexID = "FZKTRTRNFETALP3356"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_NF_ETAL_P3356', 'description': 'NF-Transformer, ETAL P3356, http://www.etalgroup.com/sites/default/files/products/P3356_December_2005.pdf', 'tags': 'NF-Transformer ETAL P3356 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_NF_ETAL_P3356.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Transformer_THT : Transformer_NF_ETAL_P3356')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

