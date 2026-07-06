class Report:

    @staticmethod
    def generate(vision, competition):

        report = {

            "product": vision.get("product_name", ""),

            "category": vision.get("category", ""),

            "keywords": vision.get("keywords", []),

            "morocco": {

                "jumia": competition["jumia"]["found"],

                "google": competition["google"]["found"],

                "tiktok": competition["tiktok"]["found"],

                "facebook": competition["facebook"]["found"]

            }

        }

        score = 0

        if report["morocco"]["jumia"]:
            score += 30

        if report["morocco"]["google"]:
            score += 20

        if report["morocco"]["tiktok"]:
            score += 30

        if report["morocco"]["facebook"]:
            score += 20

        report["score"] = score

        if score >= 70:

            report["status"] = "HIGH"

        elif score >= 40:

            report["status"] = "MEDIUM"

        else:

            report["status"] = "LOW"

        return report