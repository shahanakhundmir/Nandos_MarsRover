def outputAsString(missionData):
    for data in missionData:
        if type(data)== str:
            print(data)
        else:
            print(f"{data.x} {data.y} {data.direction}")