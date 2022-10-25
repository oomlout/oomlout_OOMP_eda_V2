
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Mount_Lodestone_VTM120"
    hexID = "FZKINLMOUNTLODESTONEVTM12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Mount_Lodestone_VTM120', 'description': 'Lodestone Pacific, 30.48mm diameter vertical toroid mount, 16AWG/1.27mm holes, http://www.lodestonepacific.com/CatKpdf/VTM_Series.pdf', 'tags': 'vertical inductor toroid mount', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Mount_Lodestone_VTM120.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Mount_Lodestone_VTM120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

