def output_as_string(missionData):
    for data in missionData:
        if type(data)== str:
            print(data)
        else:
            print(f"{data.get_x()} {data.get_y()} {data.get_direction()}")