class MoroccoDetector:

    @staticmethod
    def detect(competition):

        platforms = []

        if competition["jumia"]["found"]:
            platforms.append("Jumia")

        if competition["google"]["found"]:
            platforms.append("Google")

        if competition["facebook"]["found"]:
            platforms.append("Facebook")

        if competition["tiktok"]["found"]:
            platforms.append("TikTok")

        return {

            "available": len(platforms) > 0,

            "platforms": platforms,

            "count": len(platforms)

        }