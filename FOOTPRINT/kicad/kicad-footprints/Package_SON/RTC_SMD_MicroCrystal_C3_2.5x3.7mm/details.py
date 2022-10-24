
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "RTC_SMD_MicroCrystal_C3_2.5x3.7mm"
    hexID = "FZKSONRTCSMMXC325X37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RTC_SMD_MicroCrystal_C3_2.5x3.7mm', 'description': 'MicroCrystal C3 2.5x3.7mm, https://www.microcrystal.com/fileadmin/Media/Products/RTC/Datasheet/RV-1805-C3.pdf', 'tags': 'RTC C3', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/RTC_SMD_MicroCrystal_C3_2.5x3.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : RTC_SMD_MicroCrystal_C3_2.5x3.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

