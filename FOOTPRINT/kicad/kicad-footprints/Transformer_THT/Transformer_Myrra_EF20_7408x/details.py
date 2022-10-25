
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Myrra_EF20_7408x"
    hexID = "FZKTRTRMYRRAEF2748X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Myrra_EF20_7408x', 'description': 'EF20 flyback transformer,http://myrra.com/wp-content/uploads/2017/09/Datasheet-74087-74088-74089-rev-A.pdf', 'tags': 'transformer flyback SMPS', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Myrra_EF20_no_pin3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Transformer_THT : Transformer_Myrra_EF20_7408x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

