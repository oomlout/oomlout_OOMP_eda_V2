
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Neosid_SMS-ME3015"
    hexID = "FZKINDUCTORSMLNEOSIDSMSME315"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Neosid_SMS-ME3015', 'description': 'Neosid, Power Inductor, SMS-ME3015, Fixed inductor, SMD, magnetically shielded, https://neosid.de/import-data/product-pdf/neoFestind_SMSME3015.pdf', 'tags': 'Neosid Power Inductor SMS-ME3015 Fixed inductor SMD magnetically shielded', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_SMS-ME3015.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Neosid_SMS-ME3015')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

