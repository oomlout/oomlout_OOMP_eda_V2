
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-PD-Typ-7345"
    hexID = "FZKINDUCTORSMLWUERTHWEPDTYP7345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-PD-Typ-7345', 'description': 'Shielded Power Inductor, Wuerth Elektronik, WE-PD, SMD, 7345, https://katalog.we-online.com/pbs/datasheet/744777001.pdf', 'tags': 'Choke Shielded Power Inductor WE-PD 7345 Wuerth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-PD-Typ-7345.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-PD-Typ-7345')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

