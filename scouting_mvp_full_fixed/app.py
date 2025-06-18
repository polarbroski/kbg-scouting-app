from flask import Flask, render_template, request
from rag_llm import generate_summary_from_docs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        batting_avg = request.form["batting_avg"]
        home_runs = request.form["home_runs"]
        run_time = request.form["run_time"]
        left_handed = request.form["left_handed"]
        pop_time = request.form.get("pop_time", "")

        # 무작위 샘플 이미지 파일명 선택
        summary_filename = generate_summary_from_docs(name, [])

        return render_template("result.html", report_img=summary_filename)

    return render_template("index.html")


# ✅ Render용 entrypoint
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
