
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_CommonMode_PulseElectronics_PH9455xxx6NL_2"
    hexID = "FZKINLCOONMODEPULSEELECTRONICSPH9455XXX6NL2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_PulseElectronics_PH9455xxx6NL_2', 'description': 'common mode, inductor, filter, https://productfinder.pulseelectronics.com/api/open/product-attachments/datasheet/ph9455.105nl', 'tags': 'cmode choke dual', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_PulseElectronics_PH9455xxx6NL_2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Inductor_THT : L_CommonMode_PulseElectronics_PH9455xxx6NL_2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

