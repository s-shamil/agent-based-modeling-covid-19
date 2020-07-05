def dfToInt(df, name):

    return int(df[df["name"]==name]["value"])


def dfToFloat(df, name):

    return float(df[df["name"]==name]["value"])