import random

def generate_summary_from_docs(player_name, documents):
    # 샘플 리포트 파일명 리스트
    sample_reports = [
        "lucas_giolito.png",
        "cj_abrams.png",
        "ronald_acuna.png",
        "chance_adams.png",
        "osvaldo_abreu.png",
        "albert_abreu.png",
        "yadier_alvarez.png"
    ]
    
    # 무작위 선택
    return random.choice(sample_reports)
