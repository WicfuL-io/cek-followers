import os
import json

def load_json(path):
    if not os.path.exists(path):
        print(f"⚠️  File tidak ditemukan: {path}")
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"❌ Gagal membaca JSON: {path}")
        return []

def extract_usernames_from_list(data):
    """
    Ekstrak username dari list item JSON,
    mendukung list string, atau list dict dengan 'string_list_data' atau 'username'.
    """
    usernames = []

    if all(isinstance(item, str) for item in data):
        return [u.strip().lower() for u in data]

    for item in data:
        if isinstance(item, dict):
            if "string_list_data" in item:
                try:
                    usernames.append(item['string_list_data'][0]['value'].strip().lower())
                except (KeyError, IndexError, TypeError):
                    continue
            elif "username" in item:
                usernames.append(item['username'].strip().lower())

    return usernames

def extract_usernames(data):
    """
    Ekstrak username dari data JSON,
    bisa berupa dict dengan key 'relationships_following', 'relationships_followers', dll,
    atau list biasa.
    """
    if isinstance(data, dict):
        # Cari key yang ada isinya dan merupakan list
        for key, value in data.items():
            if isinstance(value, list) and value:
                return extract_usernames_from_list(value)
        # Jika tidak ketemu, kembalikan list kosong
        return []

    elif isinstance(data, list):
        return extract_usernames_from_list(data)
    else:
        return []

def print_list(title, user_set):
    count = len(user_set)
    print(f"\n🔹 {title} ({count} akun):")
    if count == 0:
        print("- (tidak ada)")
    else:
        for username in sorted(user_set):
            print(f"- {username}")

def main():
    folder = 'followers_and_following'

    followers_data = load_json(os.path.join(folder, 'followers_1.json'))
    following_data = load_json(os.path.join(folder, 'following.json'))
    close_friends_data = load_json(os.path.join(folder, 'close_friends.json'))
    follow_requests_received_data = load_json(os.path.join(folder, "follow_request_you've_received.json"))
    recent_follow_requests_data = load_json(os.path.join(folder, 'recent_follow_requests.json'))

    followers = set(extract_usernames(followers_data))
    following = set(extract_usernames(following_data))

    print("\nContoh followers (10):", list(followers)[:10])
    print("Contoh following (10):", list(following)[:10])

    close_friends = set(extract_usernames(close_friends_data))
    follow_requests_received = set(extract_usernames(follow_requests_received_data))
    recent_follow_requests = set(extract_usernames(recent_follow_requests_data))

    not_following_back = following - followers
    not_followed_by_you = followers - following
    mutual_follow = followers & following

    print("\n📊 Statistik Instagram")
    print(f"Total Followers            : {len(followers)}")
    print(f"Total Following            : {len(following)}")
    print(f"Mutual Followers           : {len(mutual_follow)}")
    print(f"Tidak Follow Balik         : {len(not_following_back)}")
    print(f"Kamu Tidak Follow Balik    : {len(not_followed_by_you)}")
    print(f"Close Friends              : {len(close_friends)}")
    print(f"Follow Request Diterima    : {len(follow_requests_received)}")
    print(f"Follow Request Kamu Kirim  : {len(recent_follow_requests)}")

    print_list("Tidak Follow Balik (kamu follow mereka)", not_following_back)
    print_list("Kamu Tidak Follow Balik (mereka follow kamu)", not_followed_by_you)
    print_list("Mutual Followers", mutual_follow)
    print_list("Close Friends", close_friends)
    print_list("Follow Request Diterima (masuk)", follow_requests_received)
    print_list("Follow Request Kamu Kirim", recent_follow_requests)


if __name__ == "__main__":
    main()
