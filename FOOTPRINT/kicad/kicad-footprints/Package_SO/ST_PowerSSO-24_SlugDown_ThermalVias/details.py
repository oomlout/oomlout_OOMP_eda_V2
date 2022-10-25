
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "ST_PowerSSO-24_SlugDown_ThermalVias"
    hexID = "FZKSOSTPOWERSSO24SLUGDOWNTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_PowerSSO-24_SlugDown_ThermalVias', 'description': 'ST PowerSSO-24 1EP 7.5x10.3mm Pitch 0.8mm [JEDEC MO-271] (http://www.st.com/resource/en/datasheet/tda7266p.pdf, http://freedatasheets.com/downloads/Technical%20Note%20Powersso24%20TN0054.pdf)', 'tags': 'ST PowerSSO-24 1EP 7.5x10.3mm Pitch 0.8mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/ST_PowerSSO-24_SlugDown.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : ST_PowerSSO-24_SlugDown_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

