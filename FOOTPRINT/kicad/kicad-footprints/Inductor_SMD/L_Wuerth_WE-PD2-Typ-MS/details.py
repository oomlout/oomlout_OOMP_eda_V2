
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-PD2-Typ-MS"
    hexID = "FZKINDUCTORSMLWUERTHWEPD2TYPMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-PD2-Typ-MS', 'description': 'Power Inductor, Wuerth Elektronik, WE-PD2, SMD, Typ MS, https://katalog.we-online.com/pbs/datasheet/744774022.pdf', 'tags': 'Choke Power Inductor WE-PD2 TypMS Wuerth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-PD2-Typ-MS.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-PD2-Typ-MS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

