
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Pulse_H1100NL"
    hexID = "FZKTRSMTRPULSEH11NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Pulse_H1100NL', 'description': 'For H1100NL, H1101NL, H1102NL, H1121NL, H1183NL, H1199NL, HX1188NL, HX1198NL and H1302NL. https://productfinder.pulseeng.com/doc_type/WEB301/doc_num/H1102NL/doc_part/H1102NL.pdf', 'tags': 'H1100NL H1101NL H1102NL H1121NL H1183NL H1199NL HX1188NL HX1198NL H1302N', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Pulse_H1100NL.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Pulse_H1100NL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

