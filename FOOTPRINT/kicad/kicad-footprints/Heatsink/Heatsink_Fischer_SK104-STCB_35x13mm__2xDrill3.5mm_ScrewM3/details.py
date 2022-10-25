
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_Fischer_SK104-STCB_35x13mm__2xDrill3.5mm_ScrewM3"
    hexID = "FZKHHFISCHERSK14STCB35X132XDRILL35SCREWM3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_Fischer_SK104-STCB_35x13mm__2xDrill3.5mm_ScrewM3', 'description': 'Heatsink, 35mm x 13mm, 2x Fixation 2,5mm Drill, Soldering, Fischer SK104-STC-STIC,', 'tags': 'Heatsink fischer TO-220', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_SK104-STCB_35x13mm__2xDrill3.5mm_ScrewM3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_Fischer_SK104-STCB_35x13mm__2xDrill3.5mm_ScrewM3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

