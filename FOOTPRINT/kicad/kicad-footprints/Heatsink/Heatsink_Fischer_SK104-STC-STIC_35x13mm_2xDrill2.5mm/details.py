
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_Fischer_SK104-STC-STIC_35x13mm_2xDrill2.5mm"
    hexID = "FZKHHFISCHERSK14STCSTIC35X132XDRILL25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_Fischer_SK104-STC-STIC_35x13mm_2xDrill2.5mm', 'description': 'Heatsink, 35mm x 13mm, 2x Fixation 2,5mm Drill, Soldering, Fischer SK104-STC-STIC,', 'tags': 'Heatsink fischer TO-220', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_SK104-STC-STIC_35x13mm_2xDrill2.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_Fischer_SK104-STC-STIC_35x13mm_2xDrill2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

