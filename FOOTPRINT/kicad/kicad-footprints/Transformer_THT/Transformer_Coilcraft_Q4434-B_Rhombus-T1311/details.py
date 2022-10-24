
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_THT"
    oIndex = "Transformer_Coilcraft_Q4434-B_Rhombus-T1311"
    hexID = "FZKTRTRCOILCRAFTQ4434BRHOMBUST1311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Coilcraft_Q4434-B_Rhombus-T1311', 'description': 'Transformator, Transformer, Flyback, Coilcraft Q4434-B, Rgombus T1311,', 'tags': 'Transformator Transformer Flyback Coilcraft Q4434-B Rgombus T1311 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Coilcraft_Q4434-B_Rhombus-T1311.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transformer_THT : Transformer_Coilcraft_Q4434-B_Rhombus-T1311')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

