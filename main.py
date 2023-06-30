from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_captions(video_id, api_key):
    try:
        # YouTube API 클라이언트 구성
        youtube = build("youtube", "v3", developerKey=api_key)

        # 자막 리스트 가져오기
        captions_request = youtube.captions().list(
            part="snippet",
            videoId=video_id,
        )
        response = captions_request.execute()

        # 자막 정보와 원하는 값 반환
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
    api_key = ""  # 여기에 YouTube Data API key를 입력하세요.
    captions = get_captions(video_id, api_key)

    if captions:
        for c in captions:
            print(f"{c['language']} ({c['trackKind']}): {c['id']}")
    else:
        print("No captions found")
