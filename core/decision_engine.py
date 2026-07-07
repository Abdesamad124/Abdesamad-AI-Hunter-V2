from difflib import SequenceMatcher


class DecisionEngine:

    def __init__(self):

        self.threshold = 70

    def text_similarity(self, text1, text2):

        if not text1 or not text2:

            return 0

        score = SequenceMatcher(

            None,

            text1.lower(),

            text2.lower()

        ).ratio()

        return round(score * 100, 2)

    def evaluate_product(self, vision, product):

        product_name = vision.get(

            "product_name",

            ""

        )

        category = vision.get(

            "category",

            ""

        )

        material = vision.get(

            "material",

            ""

        )

        color = vision.get(

            "color",

            ""

        )

        title = product.get(

            "title",

            ""

        )

        score = 0

        score += self.text_similarity(

            product_name,

            title

        ) * 0.60

        score += self.text_similarity(

            category,

            title

        ) * 0.20

        score += self.text_similarity(

            material,

            title

        ) * 0.10

        score += self.text_similarity(

            color,

            title

        ) * 0.10

        score = round(score, 2)

        product["ai_score"] = score

        product["accepted"] = score >= self.threshold

        return product

    def evaluate(self, vision, competition):

        matches = []

        rejected = []

        for platform, result in competition.items():

            products = result.get(

                "products",

                []

            )

            for product in products:

                item = self.evaluate_product(

                    vision,

                    product

                )

                item["platform"] = platform

                if item["accepted"]:

                    matches.append(item)

                else:

                    rejected.append(item)

        matches.sort(

            key=lambda x: x["ai_score"],

            reverse=True

        )

        rejected.sort(

            key=lambda x: x["ai_score"],

            reverse=True

        )

        confidence = 0

        if matches:

            confidence = matches[0]["ai_score"]

        return {

            "found": len(matches) > 0,

            "confidence": confidence,

            "matches": matches,

            "rejected": rejected

        }