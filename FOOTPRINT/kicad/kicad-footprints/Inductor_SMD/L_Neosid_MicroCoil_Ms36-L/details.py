
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Neosid_MicroCoil_Ms36-L"
    hexID = "FZKINDUCTORSMLNEOSIDMCOILMS36L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Neosid_MicroCoil_Ms36-L', 'description': 'Neosid, Micro Coil, Inductor, Ms36-L, SMD, Fixed inductor, anti clockwise, https://neosid.de/en/products/inductors/rod-core-chokes/smd-rod-core-chokes/52026/ms-36/7-h?c=94', 'tags': 'Neosid Micro Coil Inductor Ms36-L SMD Fixed inductor anti clockwise', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_MicroCoil_Ms36-L.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Neosid_MicroCoil_Ms36-L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

