
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-XHP70-W-CREE-01-"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLSXHP7WCREE1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LEDS-XHP70-W-CREE-01-', 'description': 'hexID: ; Cree XHP70 LED, 6V version, http://www.cree.com/~/media/Files/Cree/LED%20Components%20and%20Modules/XLamp/Data%20and%20Binning/ds%20XHP70.pdf', 'tags': 'LED Cree XHP70', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-XHP70_6V.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('oomlout_OOMP_parts : LEDS-XHP70-W-CREE-01-')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

