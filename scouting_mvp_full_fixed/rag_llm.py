import random

def generate_summary_from_docs(player_name, documents):
    sample_reports = [
        f"""
        Player: {player_name}
        OFP: 50 / Risk: Extreme / ETA: 2025

        Hit: 50 - Very raw as a hitter with a lot of mechanical tinkering needed. Flat bat path, needs consistent setup.
        Power: 40 - Needs more strength, currently limited raw pop. Could develop with swing change.
        Speed: 70 - Elite speed, top-of-the-scale runner. Covers ground fast.
        Glove: 55 - Solid fundamentals, playable at short. Could fit in CF.
        Arm: 60 - Strong accurate throws, plays up in middle infield.

        Overall: High-risk, high-reward athlete with premium speed. Must grow at the plate.
        """,

        f"""
        Player: {player_name}
        OFP: 60 / Risk: Moderate / ETA: 2018

        FB: 70 - Plus arm strength, 96 mph peak, late life. Drives off lower half.
        CB: 60 - Sharp 11-5 breaker, commands well, tough on righties.
        CH: 60 - Deceptive with late fade, consistent arm speed.
        SL: 50 - Flashed potential, not primary weapon.

        Overall: Fastball/changeup combo strong, potential mid-rotation arm with some relief risk.
        """,

        f"""
        Player: {player_name}
        OFP: 80 / Risk: Low / ETA: 2018

        Hit: 60 - Consistent hard contact, strong bat speed, compact swing.
        Power: 70 - Big raw power, explosive wrist strength. Pull-side juice.
        Speed: 55 - Solid runner, not elite but quick enough.
        Glove: 55 - Reads well in CF, solid routes.
        Arm: 70 - Accurate cannon from RF track.

        Overall: Ready for the majors now. All-Star ceiling. Three-hole hitter with defensive value.
        """
    ]

    return random.choice(sample_reports)
