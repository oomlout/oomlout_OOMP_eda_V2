
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Bourns-SRN8040_8x8.15mm"
    hexID = "FZKINDUCTORSMLBOURNSSRN848X815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Bourns-SRN8040_8x8.15mm', 'description': 'Bourns SRN8040 series SMD inductor 8x8.15mm, https://www.bourns.com/docs/Product-Datasheets/SRN8040.pdf', 'tags': 'Bourns SRN8040 SMD inductor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns-SRN8040_8x8.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Bourns-SRN8040_8x8.15mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

