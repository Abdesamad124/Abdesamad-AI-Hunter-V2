class ProductScore:

    @staticmethod
    def calculate(result):

        score = 0

        if result["competition"]["jumia"]["found"]:
            score += 35

        if result["competition"]["google"]["found"]:
            score += 20

        if result["competition"]["tiktok"]["found"]:
            score += 30

        if result["competition"]["facebook"]["found"]:
            score += 15

        if score >= 80:

            level = "EXCELLENT"

        elif score >= 60:

            level = "GOOD"

        elif score >= 40:

            level = "MEDIUM"

        else:

            level = "LOW"

        return {

            "score": score,

            "level": level

        }