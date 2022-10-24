
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Breve_TEZ-28x33"
    hexID = "FZKTRTRBREVETEZ28X33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Breve_TEZ-28x33', 'description': 'http://www.breve.pl/pdf/ANG/TEZ_ang.pdf', 'tags': 'TEZ PCB Transformer', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Breve_TEZ-28x33.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Transformer_THT : Transformer_Breve_TEZ-28x33')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

