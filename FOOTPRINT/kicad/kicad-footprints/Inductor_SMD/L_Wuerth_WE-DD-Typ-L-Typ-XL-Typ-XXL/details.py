
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-DD-Typ-L-Typ-XL-Typ-XXL"
    hexID = "FZKINDUCTORSMLWUERTHWEDDTYPLTYPXLTYPXXL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-DD-Typ-L-Typ-XL-Typ-XXL', 'description': 'Shielded Coupled Inductor, Wuerth Elektronik, WE-DD, SMD, Typ L, Typ XL, Typ XXL, https://katalog.we-online.com/pbs/datasheet/744874001.pdf', 'tags': 'Choke Coupled Double Inductor SMD Wuerth WE-DD TypL TypXL TypXXL ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-DD-Typ-L-Typ-XL-Typ-XXL.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-DD-Typ-L-Typ-XL-Typ-XXL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

