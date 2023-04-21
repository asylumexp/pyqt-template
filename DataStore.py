# need to add data


class data_store:
    def __init__(self) -> None:
        pass

    def calc_bmi(self, height, weight):
        bmi = round((weight / ((height / 100) * (height / 100))), 1)
        return bmi

    def calc_bmr(self, height, weight):
        pass
