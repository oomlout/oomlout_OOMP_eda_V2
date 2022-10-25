
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Coilcraft_CST2010"
    hexID = "FZKTRSMTRCOILCRAFTCST21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Coilcraft_CST2010', 'description': 'Current sense transformer, SMD, 14.55x19.91x10.50mm (https://www.coilcraft.com/pdfs/cst2010.pdf)', 'tags': 'Transformer current sense SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Coilcraft_CST2010.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Coilcraft_CST2010')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

