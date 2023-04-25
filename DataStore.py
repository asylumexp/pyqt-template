# need to add data


class data_store:
    def __init__(self) -> None:
        pass

    @staticmethod
    def calc_bmi(height, weight):
        bmi = round((weight / ((height / 100) * (height / 100))), 1)
        return bmi

    @staticmethod
    def calc_bmr(height, weight, age, sex):
        if sex == "male":
            return 88.362 + (18.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            return 447.593 + (0.247 * weight) + (3.098 * height) - (4.330 * age)
