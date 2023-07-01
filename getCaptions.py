from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_captions(video_id, api_key):
    try:
        youtube = build("youtube", "v3", developerKey=api_key)

        captions_request = youtube.captions().list(
            part="snippet",
            videoId=video_id,
        )
        response = captions_request.execute()

        captions = []
        for item in response["items"]:
            caption_data = {
                "id": item["id"],
                "language": item["snippet"]["language"],
                "trackKind": item["snippet"]["trackKind"],
            }
            captions.append(caption_data)
        return captions
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None

if __name__ == "__main__":
    video_id = "mR8TS7kkFEk"
    api_key = ""
    captions = get_captions(video_id, api_key)

    if captions:
        for c in captions:
            print(f"{c['language']} ({c['trackKind']}): {c['id']}")
    else:
        print("No captions found")
