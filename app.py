from flask import Flask, render_template, request
import zipfile, json, os, tempfile

app = Flask(__name__)

# ================= PARSER PALING AMAN =================
def extract_usernames(data):
    usernames = set()

    def walk(obj):
        if isinstance(obj, dict):
            if "string_list_data" in obj:
                try:
                    usernames.add(obj["string_list_data"][0]["value"].lower())
                except:
                    pass
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for i in obj:
                walk(i)

    walk(data)
    return usernames

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# ================= ROUTE =================
@app.route("/", methods=["GET", "POST"])
def index():
    stats = None

    if request.method == "POST":
        file = request.files["file"]
        temp_dir = tempfile.mkdtemp()

        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        base = os.path.join(
            temp_dir,
            "followers_and_following"
        )

        followers = extract_usernames(
            load_json(os.path.join(base, "followers_1.json"))
        )
        following = extract_usernames(
            load_json(os.path.join(base, "following.json"))
        )

        mutual = followers & following

        stats = {
            "followers": len(followers),
            "following": len(following),
            "mutual": len(mutual),
            "followers_list": sorted(followers),
            "following_list": sorted(following),
            "not_following_back": sorted(following - followers),
            "not_followed_by_you": sorted(followers - following),
        }

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
