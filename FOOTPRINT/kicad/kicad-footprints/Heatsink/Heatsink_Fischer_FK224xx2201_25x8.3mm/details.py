
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_Fischer_FK224xx2201_25x8.3mm"
    hexID = "FZKHHFISCHERFK224XX22125X83"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_Fischer_FK224xx2201_25x8.3mm', 'description': '25x8.3mm Heatsink, 18K/W, TO-220, https://www.fischerelektronik.de/web_fischer/en_GB/$catalogue/fischerData/PR/FK224_220_1_/datasheet.xhtml?branch=heatsinks', 'tags': 'heatsink TO-220', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_FK2242201_25x8.3mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_Fischer_FK224xx2201_25x8.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

