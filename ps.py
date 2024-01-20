import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API 인증 설정
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="YOUR_REDIRECT_URI",
        scope="user-library-read"  # 필요한 권한 설정
    )
)

# 예제: 사용자의 저장된 플레이리스트 목록 가져오기
results = sp.current_user_playlists()
for playlist in results['items']:
    print(playlist['name'])
