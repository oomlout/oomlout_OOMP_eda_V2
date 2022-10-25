
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Murata_LQH2MCNxxxx02_2.0x1.6mm"
    hexID = "FZKINDUCTORSMLMLQH2MCNXXXX22X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Murata_LQH2MCNxxxx02_2.0x1.6mm', 'description': 'Inductor, Murata, LQH2MCN_02 series, 1.6x2.0x0.9mm (https://search.murata.co.jp/Ceramy/image/img/P02/JELF243A-0053.pdf)', 'tags': 'chip coil inductor Murata LQH2MC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Murata_LQH2MCNxxxx02_2.0x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Murata_LQH2MCNxxxx02_2.0x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

